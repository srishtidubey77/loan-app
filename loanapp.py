from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class LoanInput(BaseModel):
    Gender: int
    Married: int
    Education: int
    ApplicantIncome: float
    LoanAmount: float
    Credit_History: int

@app.get("/")
def home():
    return {"message": "Loan Prediction API is live"}

@app.post("/predict")
def predict(data: LoanInput):
    features = [[
        data.Gender,
        data.Married,
        data.Education,
        data.ApplicantIncome,
        data.LoanAmount,
        data.Credit_History
    ]]
    prediction = model.predict(features)
    return {"loan_approved": bool(prediction[0])}
