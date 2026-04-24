import os
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
from dotenv import load_dotenv

load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

url = "https://appbrewery.github.io/instant_pot/"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

price_tag = soup.select_one(".a-offscreen")
price_text = price_tag.get_text()
price = float(price_text.replace("$", ""))

if price < 100:
    title_tag = soup.find("span", id="productTitle").get_text().split()
    title = " ".join(title_tag)

    with SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{title} is now {price}\n{url}"
        )