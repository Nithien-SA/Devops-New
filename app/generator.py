# app/generator.py
import random
import time

def generate_sensor_data():
    """
    Generate mock IoT sensor data for temperature, humidity, and light.
    """
    data = {
        "temperature": round(random.uniform(20.0, 35.0), 2),   # °C
        "humidity": round(random.uniform(40.0, 90.0), 2),      # %
        "light": round(random.uniform(100, 1000), 2),          # lumens
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return data
