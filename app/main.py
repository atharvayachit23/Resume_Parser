

from fastapi import FastAPI, UploadFile, File, Form, HTTPException

from app.parser import parse_resume, parse_job_description
from app.matcher import match_resume
from app.schema import MatchResult

app = FastAPI(
    title="AI Resume Matcher",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Matcher API is running."
    }


@app.post(
    "/analyze",
    response_model=MatchResult
)
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]

    if resume.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    parsed_resume = parse_resume(resume)

    parsed_job = parse_job_description(job_description)

    result = match_resume(
        parsed_job,
        parsed_resume
    )

    return result