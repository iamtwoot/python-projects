import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

GENDER = "male"
AGE = 26
HEIGHT = 188
WEIGHT = 78

# Nutrition and Exercise API
nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
query = input("Enter exercise (one at a time): ")
data = {
    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}
response = requests.post(
    url=nutrition_endpoint,
    headers=nutrition_headers,
    json=data,
)
response.raise_for_status()
print(response.json())
exercise = response.json()["exercises"][0]


# Sheety API
sheety_post_endpoint = "https://api.sheety.co/a88fb946c8c271239ada21877e03dd4b/workoutTracker20/workouts"

day = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}
data = {
    "workout": {
        "date": day,
        "time": time,
        "exercise": exercise["name"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
}

sheety_response = requests.post(url=sheety_post_endpoint, headers=headers, json=data)
sheety_response.raise_for_status()

