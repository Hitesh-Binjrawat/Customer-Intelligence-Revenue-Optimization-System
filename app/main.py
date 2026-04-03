# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from src.decision_engine import predict_customer

app = FastAPI(title="Customer Intelligence API")


# Input schema
class CustomerInput(BaseModel):
    recency: float
    frequency: float
    monetary: float


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: CustomerInput):
    result = predict_customer(
        recency=data.recency,
        frequency=data.frequency,
        monetary=data.monetary
    )
    return result