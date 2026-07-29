from pydantic import BaseModel

class ResumeFeatures(BaseModel):
    python: int
    sql: int
    docker: int
    projects: int
    experience_years: int
    ats_score: int