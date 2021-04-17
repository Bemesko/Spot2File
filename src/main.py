import utils.client_keys as client_keys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id = client_keys.CLIENT_ID, client_secret=client_keys.CLIENT_SECRET)
spotify = spotipy.Spotify(auth_manager=auth_manager)

playlist = spotify.playlist_items("2I1y0a2GYPdGHlUXW1JPwF")
while playlist:
    for i, playlist_song in enumerate(playlist['items']):
        print(f"{i} - '{playlist_song['track']['name']}' by '{playlist_song['track']['artists'][0]['name']}'")
    if playlist['next']:
       playlist = spotify.next(playlist) 
    else:
        playlist = None