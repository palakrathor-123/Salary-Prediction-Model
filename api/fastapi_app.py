from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predictor import predict_salary

app = FastAPI()


class SalaryInput(BaseModel):
    experience: int
    education: str
    job_role: str
    location: str
    skills: int


@app.get("/")
def home():
    return {"message": "Salary Prediction API Running"}


@app.post("/predict")
def predict(data: SalaryInput):
    salary = predict_salary(
        data.experience,
        data.education,
        data.job_role,
        data.location,
        data.skills
    )

    return {
        "best_model": "Ridge Regression",
        "predicted_salary": salary
    }