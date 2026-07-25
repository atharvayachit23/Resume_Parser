from app.llm import call_llm
from app.prompts import get_match_prompt
from app.schema import MatchResult


def match_resume(job, resume) -> MatchResult:
    """
    Compare a parsed resume with a parsed job description
    and return the match result.
    """

    match_schema = MatchResult.model_json_schema()

    job_json = job.model_dump_json(indent=2)
    resume_json = resume.model_dump_json(indent=2)

    system_prompt = get_match_prompt(
        job_json=job_json,
        resume_json=resume_json,
        schema=match_schema
    )

    data = call_llm(
        system_prompt=system_prompt,
        user_prompt=""
    )

    return MatchResult(**data)