import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/bakeboard-hot-100/"

prompt = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{url}{prompt}")
response.raise_for_status()
html = response.text
