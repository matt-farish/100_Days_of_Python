#Day 46 of Udemy's 100 Days of Python programming course
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

# =============== TOP 100 BILLBOARD SCRAPING ===============

date = input("What date to you wish to travel to? Type the date in the format: YYYY-MM-DD: ")
year = date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
music_web_page = response.text

soup = BeautifulSoup(music_web_page, "html.parser")

# data = soup.select(selector = "li h3")
hot_100_songs = [song.getText().strip("\n\t") for song in soup.select(selector = "li h3")]

hot_100_artists = [artist.getText().strip("\t\n") for artist in soup.find_all(name="span", class_="c-label")]

songs = hot_100_songs[:100]
artists = [artist.split(" Featuring")[0].split(" Duet")[0] for artist in hot_100_artists
            if not artist.isnumeric()
            if artist != "-"
            if artist != "NEW"
            if "ENTRY" not in artist 
            ]

# =============== SPOTIFY API ===============

CLIENT_ID = config("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")
USER_ID = config("SPOTIFY_USER_ID")
USER_NAME = config("SPOTIFY_USER_NAME")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        show_dialog = True,
        cache_path = "token.txt"
    )
)

song_urls = []

for song, artist in zip(songs, artists):
    items = sp.search(q = f"track: {song}, artist: {artist} type = 'track'")["tracks"]["items"]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = sp.user_playlist_create(user = USER_ID, name=f"{date} Billboard 100", public = False)["id"]

sp.playlist_add_items(playlist_id = playlist_id, items = song_urls)