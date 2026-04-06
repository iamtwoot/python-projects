import smtplib
import time
import requests
from datetime import datetime
from zoneinfo import ZoneInfo
import os

def get_env(name):
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Environment variable {name} not set.")
    return value

MY_EMAIL = get_env("MY_EMAIL")
MY_PASSWORD = get_env("MY_PASSWORD")

MY_LAT = 56.376859 # Your latitude
MY_LONG = 44.042414 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_position_within(iss_lat, iss_long):
    if ((MY_LAT - 5 < iss_lat < MY_LAT + 5) and
            (MY_LONG - 5 < iss_long < MY_LONG + 5)):
        return True
    return False

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

time_now = datetime.now(ZoneInfo("Europe/Moscow")).hour

while True:
    if is_position_within(iss_latitude, iss_longitude):
        if sunset < time_now < sunrise:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject: Look up!\n\nLook up! ISS is currently flying above you.",
                )
    time.sleep(60)