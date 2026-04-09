import requests

api_key = "dd84ad89a0b92d7c94f5b5f73977aae0"
lat = 56.376847
lon = 44.042441

params = {
    "lat": lat,
    "lon": lon,
    "cnt": 4,
    "appid": api_key,
}

url = f"https://api.openweathermap.org/data/2.5/forecast"

def send_sms():
    print("Sending message...")
    print("It will rain today.")

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()

weather_id_list = []
will_rain = False
for three_hour_data in weather_data["list"]:
    weather_id = three_hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    send_sms()

