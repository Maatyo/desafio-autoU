#   Classificador Inteligente de Emails  
### Produtivo x Improdutivo com FastAPI e NLP

Este projeto é uma aplicação web desenvolvida em **Python utilizando FastAPI**, cujo objetivo é **classificar emails automaticamente** em duas categorias principais:

- **  Produtivo** → Emails que exigem ação, suporte técnico ou resolução de problemas  

- **  Improdutivo** → Emails informativos, elogios ou mensagens que não demandam ação  

Além da classificação, o sistema **gera automaticamente uma resposta profissional**, adequada ao tipo de email recebido.

---

##  Objetivo do Projeto

Este projeto foi desenvolvido como parte de um **desafio técnico (nível Júnior Full Stack)** e tem como objetivo demonstrar:

- Aplicação prática de **Inteligência Artificial e NLP**
- Implementação de **regras de negócio claras**
- Integração entre **backend (FastAPI)** e **frontend (HTML + CSS)**
- Organização de código e boas práticas
- Capacidade de resolver problemas técnicos de forma autônoma

---

##  Funcionalidades

✔ Classificação automática de emails  
✔ Identificação de emails **Produtivos** e **Improdutivos**  
✔ Geração de resposta automática adequada à categoria  
✔ Detecção automática de idioma (Português ou Inglês)  
✔ Interface web simples, intuitiva e responsiva  
✔ Feedback visual por cores (verde e vermelho)  
✔ Loader visual durante o processamento  
✔ Tratamento de emails ambíguos  

---

## Como funciona a classificação?

A classificação utiliza uma **abordagem híbrida**, combinando:

###  Regras de Negócio (Palavras-chave)

O sistema analisa o texto do email procurando termos relevantes.

#### 🔹 Emails Produtivos
Palavras-chave comuns:
- problema
- erro
- ajuda
- suporte
- acesso
- falha
- não consigo
- issue
- error
- support

Esses emails normalmente indicam **problemas ativos que exigem ação**.

#### 🔹 Emails Improdutivos
Palavras-chave comuns:
- obrigado
- agradeço
- parabéns
- satisfeito
- resolvido
- excelente atendimento
- thank you
- appreciate

Esses emails **não exigem ação imediata**.

 Caso um email contenha termos de ambos os tipos, a regra prioriza **Produtivo**, pois requer atendimento.

---

###  Uso de IA (Fallback)

Quando o email **não se enquadra claramente nas regras**, o sistema utiliza um **modelo de linguagem da Hugging Face (MT5)** para auxiliar na classificação.

 A IA é utilizada **apenas como suporte**, garantindo estabilidade, previsibilidade e coerência no resultado final.

---

##  Suporte a Idiomas

O sistema detecta automaticamente se o email está em:

- 🇧🇷 Português  
- 🇺🇸 Inglês  

 **Independentemente do idioma do email**, a resposta final ao usuário é **sempre retornada em português**, conforme regra de negócio definida no projeto.

---

##  Interface Web

A aplicação conta com uma interface simples e funcional, permitindo:

- Inserção do texto do email
- Visualização da categoria identificada
- Exibição da resposta automática
- Destaque visual da classificação:
  -  Verde → Produtivo  
  -  Vermelho → Improdutivo  

O foco foi manter uma experiência **limpa, intuitiva e objetiva**.

---

##  Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **Transformers (Hugging Face)**
- **HTML5**
- **CSS3**
- **Jinja2**
- **Uvicorn**

---

## Como executar o projeto localmente

1. Crie o ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

2. Instale as dependências:
   pip install -r requirements.txt

3. Execute a aplicação:
   uvicorn app.main:app --reload

4. Acesse:
   http://127.0.0.1:8000/docs

##  Estrutura do Projeto


```bash
app/
├── main.py
├── services/
│   └── ai_service.py
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
