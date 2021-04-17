import utils.client_keys as client_keys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id = client_keys.CLIENT_ID, client_secret=client_keys.CLIENT_SECRET)
spotify = spotipy.Spotify(auth_manager=auth_manager)

playlists = spotify.user_playlists('bmendoim')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(f"{i + 1 + playlists['offset']} {playlist['uri']} {playlist['name']}")
    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None