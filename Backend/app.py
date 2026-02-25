from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
from typing import Dict
import numpy as np
import joblib
import json
import os

app = FastAPI(title="Student Productivity ML API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "pkl models")

REGRESSOR = joblib.load(os.path.join(MODEL_DIR, "regressor.pkl"))
CLASSIFIER = joblib.load(os.path.join(MODEL_DIR, "classifier.pkl"))
SCALER = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))

with open(os.path.join(MODEL_DIR, "preprocess.json"), "r") as f:
    PREPROCESS = json.load(f)

FEATURE_ORDER = PREPROCESS["feature_order"]


REQUIRED_FIELDS = [
    "study_hours_per_day", "sleep_hours", "phone_usage_hours", "social_media_hours",
    "youtube_hours", "gaming_hours", "stress_level", "focus_score",
    "attendance_percentage", "exercise_minutes", "coffee_intake_mg",
    "assignments_completed", "final_grade"
]

class PredictRequest(BaseModel):
    study_hours_per_day: Optional[float] = None
    sleep_hours: Optional[float] = None
    phone_usage_hours: Optional[float] = None
    social_media_hours: Optional[float] = None
    youtube_hours: Optional[float] = None
    gaming_hours: Optional[float] = None
    stress_level: Optional[int] = None
    focus_score: Optional[int] = None
    attendance_percentage: Optional[float] = None
    exercise_minutes: Optional[int] = None
    coffee_intake_mg: Optional[int] = None
    assignments_completed: Optional[int] = None
    final_grade: Optional[float] = None


@app.post("/predict")
def predict(payload: PredictRequest):
    x_dict = payload.dict()

    missing = [field for field in REQUIRED_FIELDS if x_dict.get(field) is None]
    if missing:
        return {
            "status": "missing_fields",
            "missing_fields": missing
        }

    x = np.array([[x_dict[col] for col in FEATURE_ORDER]])
    x_scaled = SCALER.transform(x)

    score = float(REGRESSOR.predict(x_scaled)[0])
    label = str(CLASSIFIER.predict(x_scaled)[0])

    return {
        "status": "ok",
        "productivity_score": round(score, 2),
        "label": label
    }