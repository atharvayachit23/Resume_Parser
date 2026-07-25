from app.config import settings
from app.prompts import get_job_description_prompt,get_resume_parser_prompt
from app.schema import Resume,JobDescription
from app.llm import client,call_llm
import json
from app.utils import extract_resume_text

def parse_job_description(job_description: str) -> JobDescription:
    """
    Parses a job description into a structured JobDescription object.
    """

    schema = JobDescription.model_json_schema()

    system_prompt = get_job_description_prompt(schema)

    user_prompt = f"""
    Analyze the following job description:

    {job_description}
    """

    data = call_llm(system_prompt, user_prompt)

    return JobDescription(**data)


def parse_resume(file) -> Resume:
    """
    Parses an uploaded resume into a structured Resume object.
    """

    resume_text = extract_resume_text(file)

    schema = Resume.model_json_schema()

    system_prompt = get_resume_parser_prompt(schema)

    user_prompt = f"""
    Parse the following resume:

    {resume_text}
    """

    data = call_llm(system_prompt, user_prompt)

    return Resume(**data)