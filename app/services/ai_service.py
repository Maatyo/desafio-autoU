from transformers import pipeline

# Pipeline simples de fallback AI
classifier_ai = pipeline(
    "text2text-generation",
    model="google/mt5-small"
)

# Palavras-chave
PRODUCTIVE_KEYWORDS = [
    "problema", "erro", "ajuda", "suporte",
    "acesso", "falha", "não consigo", "dificuldade",
    "problem", "error", "help", "support",
    "access", "cannot", "issue"
]

IMPRODUCTIVE_KEYWORDS = [
    "obrigado", "agradeço", "agradecimento",
    "parabéns", "satisfeito", "resolvido",
    "funcionando perfeitamente",
    "thank you", "thanks", "appreciate",
    "great service", "working perfectly"
]

# Detecta idioma
def detect_language(text: str) -> str:
    text_lower = text.lower()
    portuguese_markers = ["obrigado", "problema", "ajuda", "acesso", "sistema", "falha", "não consigo", "dificuldade", "atendimento", "suporte", "funcionando"]
    english_markers = ["thank you", "problem", "help", "support", "access", "system", "cannot", "issue", "working", "service"]
    pt_score = sum(word in text_lower for word in portuguese_markers)
    en_score = sum(word in text_lower for word in english_markers)
    return "en" if en_score > pt_score else "pt"

# Classificação fallback AI
def ai_classify_email(text: str) -> str:
    prompt = f"Classifique o email abaixo como Produtivo ou Improdutivo. Responda apenas com uma palavra.\n\nEmail:\n{text}"
    result = classifier_ai(prompt, max_new_tokens=5)[0]["generated_text"].lower()
    return "Produtivo" if "produtivo" in result else "Improdutivo"

def classify_email(text: str):
    text_lower = text.lower()
    language = detect_language(text)

    # Regras claras primeiro
    if any(word in text_lower for word in IMPRODUCTIVE_KEYWORDS):
        category = "Improdutivo"
    elif any(word in text_lower for word in PRODUCTIVE_KEYWORDS):
        category = "Produtivo"
    else:
        category = ai_classify_email(text)

    # Respostas automáticas
    if category == "Produtivo":
        response = (
            "Olá! Obrigado por entrar em contato. "
            "Sua solicitação foi recebida e será analisada pela nossa equipe de suporte. "
            "Retornaremos o mais breve possível."
        )
    else:
        response = (
            "Agradecemos sua mensagem e o seu contato. "
            "Ficamos à disposição caso precise de qualquer suporte adicional."
        )

    return category, response
