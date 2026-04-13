import os
import requests
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

base_url = "https://app.100daysofpython.dev"
post_endpoint = f"{base_url}/v1/nutrition/natural/exercise"

data = {
    "query": input("Which exercise you did: "),
}

response = requests.post(url=post_endpoint, headers=headers, json=data)
response.raise_for_status()
