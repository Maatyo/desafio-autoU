from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import PyPDF2
from app.services.ai_service import classify_email

app = FastAPI()

# Arquivos estáticos (CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates HTML
templates = Jinja2Templates(directory="app/templates")

def preprocess_text(text: str) -> str:
    """Pré-processa o texto: remove espaços extras e normaliza."""
    return " ".join(text.split())

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_email(
    request: Request,
    email_text: str = Form(""),
    email_file: UploadFile | None = File(None)
):
    # Leitura do arquivo se houver
    if email_file and email_file.filename != "":
        if email_file.filename.endswith(".txt"):
            email_text = (await email_file.read()).decode("utf-8")
        elif email_file.filename.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(email_file.file)
            email_text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    email_text += text + "\n"
        else:
            return templates.TemplateResponse(
                "index.html",
                {"request": request, "error": "Formato não suportado. Use .txt ou .pdf."}
            )

    # Pré-processamento do texto
    email_text = preprocess_text(email_text)

    # Verifica se há texto
    if not email_text.strip():
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "Insira texto ou envie um arquivo."}
        )

    # Classificação e resposta
    category, response = classify_email(email_text)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "category": category, "response": response, "email_text": email_text}
    )
