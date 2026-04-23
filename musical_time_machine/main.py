import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# prompt = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names = [tag.getText() for tag in soup.select("h3.chart-entry__title")]
