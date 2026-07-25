AI-Resume-Matcher/
│
├── app/
│   ├── main.py              ← FastAPI entry point
│   ├── schemas.py           ← Pydantic models
│   ├── parser.py            ← Resume & JD parsing
│   ├── matcher.py           ← Matching logic
│   ├── prompts.py           ← All LLM prompts
│   ├── llm.py               ← Groq client
│   ├── utils.py             ← PDF/DOCX helpers
│   └── config.py            ← Environment variables
│
├── frontend/
│   └── app.py               ← Streamlit UI
│
├── uploads/
├── .env
├── requirements.txt
└── README.md