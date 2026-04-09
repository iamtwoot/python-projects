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

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)