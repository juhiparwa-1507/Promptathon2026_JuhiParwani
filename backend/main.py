from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Smart Hospital Command Center")


class Patient(BaseModel):
    name: str
    age: int
    symptoms: str


@app.get("/")
def home():
    return {
        "message": "Smart Hospital Backend Running"
    }


@app.post("/patient")
def patient_analysis(patient: Patient):

    if "chest pain" in patient.symptoms.lower():
        risk = "Critical"
        score = 100
    else:
        risk = "Moderate"
        score = 50

    return {
        "patient_name": patient.name,
        "risk_level": risk,
        "risk_score": score,
        "agent": "Reception Agent"
    }
