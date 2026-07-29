import joblib

model = joblib.load("saved_models/resume_model.pkl")

def predict_resume(features):
    prediction = model.predict([features])
    return int(prediction[0])