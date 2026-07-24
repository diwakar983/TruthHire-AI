from pydantic import BaseModel

class ResumeFeatures(BaseModel):
    python: int
    sql: int
    docker: int
    projects: int
    experience_years: int
    ats_score: int
    
from fastapi import APIRouter
from app.schemas.prediction import ResumeFeatures
from app.services.ml_predictor import predict_resume

router = APIRouter()


@router.post("/predict")
def predict(data: ResumeFeatures):
    features = [
     data.python,
     data.sql,
     data.docker,
     data.projects,
     data.experience_years,
     data.ats_score
    ]
    result = predict_resume(features)

    if result == 1:
     return {"prediction": "Selected"}

    return {"prediction": "Rejected"}    
