import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[2] / "saved_models" / "resume_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_resume(features):
    prediction = model.predict([features])
    return int(prediction[0])