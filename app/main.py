# app/main.py
from fastapi import FastAPI
from app.generator import generate_sensor_data

app = FastAPI(title="Mock IoT Data API", version="1.0")

@app.get("/")
def root():
    return {"message": "Mock IoT Data API is running!"}

@app.get("/sensor")
def get_sensor_data():
    """
    Endpoint to get mock sensor data
    """
    data = generate_sensor_data()
    return data
