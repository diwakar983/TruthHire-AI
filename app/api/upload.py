from fastapi import APIRouter,  UploadFile, File
import shutil
import os

from app.services.pdf_reader import extract_text

from app.utils.skill_extractor import extract_skills   

from app.services.ats_analyzer import calculate_ats    

from app.services.truth_detector import detect_truth     

from app.services.llm_service import analyze_resume

from app.services.ml_predictor import predict_resume
router = APIRouter()

@router.post("/upload")
def upload_resume(file: UploadFile= File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path=f"uploads/{file.filename}"
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    text = extract_text(file_path)
    skills = extract_skills(text)
 
    ats_data = calculate_ats(skills)
    ats = ats_data["ats_score"]
    truth=detect_truth(text,skills)
    
    features = [
    1 if "python" in skills else 0,
    1 if "sql" in skills else 0,
    1 if "docker" in skills else 0,
    2,      # Temporary projects
    1,      # Temporary experience
    ats
]
    print(features)
    print(type(ats))
    print(ats)
    prediction = predict_resume(features)

    print(text)        
    
    prompt = f"""
You are an experienced HR recruiter.

Analyze the following resume.

Resume:
{text}

ATS Score:
{ats}

Truth Score:
{truth}

Give:
1. Resume Summary
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions for improvement
"""

    ai_response = analyze_resume(prompt) 
    
 
    return{
        "filename":file.filename,
        "skills":skills,
        "ats" : ats_data,
        "truth":truth,
        "text": text[:1000],
        "prediction": "Selected" if prediction == 1 else "Rejected" ,
        "ai_feedback": ai_response,
    } 