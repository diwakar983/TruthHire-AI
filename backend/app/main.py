from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router
from app.api.predict import router as predict_router

app = FastAPI(
    title="TruthHire AI API",
    version="1.0.0"
)

app.include_router(router)
app.include_router(predict_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "TruthHire AI Backend is Running 🚀"
    }