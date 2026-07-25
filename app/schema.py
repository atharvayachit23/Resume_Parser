from pydantic import BaseModel, Field

class JobDescription(BaseModel):
    role:str
    required_skills:list[str]
    preferred_skills:list[str]
    minimum_exp:float | None = None
    educational_req: list[str]
    responsibilities: list[str]

class Experience(BaseModel):
    company:str | None = None
    role: str | None = None
    duration: str | None = None
    description: str | None = None
    skills_used: list[str] = Field(default_factory=list)

class Resume(BaseModel):
    name: str |None = None
    email: str | None = None
    phone: str | None = None
    total_experience: float | None = None
    skills: list[str] = Field(default_factory=list)
    experiences: list[Experience] = Field(default_factory=list)
    education: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)

class MatchResult(BaseModel):
    score: float
    verdict: str
    matching_skills: list[str] = Field(default_factory=list)
    missing_skills: list[str] = Field(default_factory=list)
    tips: list[str] = Field(default_factory=list)