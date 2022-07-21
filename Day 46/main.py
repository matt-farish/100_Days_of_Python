#Day 46 of Udemy's 100 Days of Python programming course
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

# =============== TOP 100 BILLBOARD SCRAPING ===============

# Prompt the user for a date.
date = input("What date to you wish to travel to? Type the date in the format: YYYY-MM-DD: ")
# Take the year value from the provided date.
year = date.split("-")[0]

# Get the data from the Billboard page matching the date provided and change it to a text web page.
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
music_web_page = response.text

# Create soup out of the web page.
soup = BeautifulSoup(music_web_page, "html.parser")

# Create a list out of the songs present in the soup by using CSS selectors.
hot_100_songs = [song.getText().strip("\n\t") for song in soup.select(selector = "li h3")]

# Create a list out of the artists present in the soup by using CSS selectors.
hot_100_artists = [artist.getText().strip("\t\n") for artist in soup.find_all(name="span", class_="c-label")]

# The songs selected are made up of the first 100 items in the song list.
songs = hot_100_songs[:100]

# Create a list of artists by assuring the artist entry matches a number of conditions.
artists = [artist.split(" Featuring")[0].split(" Duet")[0] for artist in hot_100_artists
            if not artist.isnumeric()
            if artist != "-"
            if artist != "NEW"
            if "ENTRY" not in artist 
            ]

# =============== SPOTIFY API ===============

# Variables that will be used to authenticate Spotify access.
CLIENT_ID = config("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")
USER_ID = config("SPOTIFY_USER_ID")

# A Spotipy object that allows access to the Spotipy API
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

# Create an empty list that song URIs will be added into.
song_uris = []

# For every song and associated artist, search spotify for the track and if it exists, add its URI to the list.
for song, artist in zip(songs, artists):
    items = sp.search(q = f"track: {song}, artist: {artist} type = 'track'")["tracks"]["items"]
    if len(items) > 0:
        song_uris.append(items[0]["uri"])

# Create a new playlist on the selected user, using the date as the first title element.
playlist_id = sp.user_playlist_create(user = USER_ID, name=f"{date} Billboard 100", public = False)["id"]

# Using the previously created playlist ID, add the songs present in the song_uris list to the playlist.
sp.playlist_add_items(playlist_id = playlist_id, items = song_uris)