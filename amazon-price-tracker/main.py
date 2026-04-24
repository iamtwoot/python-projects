import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/instant_pot/"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

price_tag = soup.select_one(".a-offscreen")
price_text = price_tag.get_text()
price = float(price_text.replace("$", ""))
