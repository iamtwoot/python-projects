import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names = [tag.getText() for tag in soup.select("h3.chart-entry__title")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://example.com",
    scope="playlist-modify-private user-library-read",
))
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    song = song.strip()
    result = sp.search(q=f"track: {song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn`t exist in Spotify. Skipped.")

new_playlist = sp.current_user_playlist_create(
    name=f"{date} Billboard 100",
    public=False,
    description=f"Created using Python",
)
new_playlist_id = new_playlist["id"]

sp.playlist_add_items(new_playlist_id, song_uris)