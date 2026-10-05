# LegalEase - AI-Powered Legal Document Generator

A student project based on the provided LegalEase project specification.

## Features

- Generate legal document drafts using Google Gemini
- FastAPI backend with POST `/generate`
- Streamlit frontend
- Editable generated document
- Download as TXT, DOCX, or PDF
- Basic professional formatting
- Environment variable for API key

## Project Structure

```text
LegalEase/
├── app.py
├── main.py
├── routes.py
├── requirements.txt
├── .env.example
├── .gitignore
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py
└── utils/
    ├── __init__.py
    └── document_utils.py
```

## Setup

### 1. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini

Copy `.env.example` to `.env` and put your Gemini API key in:

```text
GEMINI_API_KEY=your_key_here
```

Do not share the API key publicly.

### 4. Start the FastAPI backend

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### 5. Start the Streamlit frontend

Open a second terminal in the same project folder:

```bash
streamlit run app.py
```

Then open the Streamlit URL shown in the terminal.

## Important

This application generates drafts for educational/general informational use. Generated legal content should be reviewed by a qualified legal professional before real-world use.
