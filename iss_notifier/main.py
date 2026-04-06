import os
import smtplib
import time
import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

if not MY_EMAIL or not MY_PASSWORD:
    raise ValueError("Email or password not set in environment variables")

MY_LAT = 56.376859 # Your latitude
MY_LONG = 44.042414 # Your longitude


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


def is_position_within(latitude, longitude):
    print(f"My position: {MY_LAT}, {MY_LONG}")
    print(f"ISS position: {latitude}, {longitude}")
    if ((MY_LAT - 5 < latitude < MY_LAT + 5) and
            (MY_LONG - 5 < longitude < MY_LONG + 5)):
        return True
    return False

def is_night():
    time_now = datetime.now(ZoneInfo("Europe/Moscow")).hour

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

def send_email():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Look up!\n\nLook up! ISS is currently flying above you.",
        )

while True:
    iss_lat, iss_long = get_iss_position()
    if is_position_within(iss_lat, iss_long):
        if is_night():
            send_email()

    time.sleep(60)