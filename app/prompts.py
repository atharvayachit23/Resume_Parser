def get_job_description_prompt(schema):
    return f"""
    You are an expert HR assistant.

    Your job is to analyze job descriptions and extract
    structured information from them.

    Return ONLY valid JSON matching this schema:

    {schema}

    IMPORTANT:
    Do NOT return the schema itself.
    Do NOT return fields like "properties", "title" or "type".
    Fill the schema with actual information extracted from the job description.

    If minimum experience is not mentioned, return null.
    If information for a list is missing, return an empty list.
    Do not invent information.
    """

def get_resume_parser_prompt(schema):
    return f"""
You are an expert resume parser.

    Extract information from the resume based on its meaning,
    not only based on exact section headings.

    Different resumes may use different headings.

    For example:
    - Experience
    - Professional Experience
    - Work History
    - Employment
    - Internships

    These may all contain relevant experience.

    Skills may also appear in the skills section, work experience,
    internships or projects.

    Return ONLY valid JSON matching this schema:

    {schema}

    Important rules:

    1. Do not invent information.
    2. If a value is not available, return null.
    3. If a list has no information, return an empty list.
    4. Include internships inside experiences.
    5. Extract skills mentioned across the entire resume.
    """

def get_match_prompt(job_json, resume_json, schema):
    return f"""
    You are an experienced HR recruiter and resume evaluator.

    Compare the candidate's resume with the given job description.

    JOB DESCRIPTION:
    {job_json}

    CANDIDATE RESUME:
    {resume_json}

    Return ONLY valid JSON matching this schema:

    {schema}

    Instructions:

    1. Calculate an overall match score from 0 to 100.
    2. List only the skills that match the job requirements.
    3. List the important skills missing from the candidate's resume.
    4. Write a short verdict (2-3 sentences) explaining how well the candidate fits the role.
    5. Give exactly 3 practical and personalized tips that would improve the candidate's chances for this specific job.
    6. Do not invent information that is not present in the resume or job description.
    7. Return ONLY valid JSON. Do not include markdown, explanations, or any extra text outside the JSON object.
    """