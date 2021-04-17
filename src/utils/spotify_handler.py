import utils.client_keys as client_keys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyHandler():
    def __init__(self) -> None:
        auth_manager = SpotifyClientCredentials(
            client_id=client_keys.CLIENT_ID, client_secret=client_keys.CLIENT_SECRET)
        self.spotify_api = spotipy.Spotify(auth_manager=auth_manager)

    def get_playlist_song_info(self, playlist_id) -> list:
        playlist = self.spotify_api.playlist_items(playlist_id)
        playlist_song_info = []

        while playlist:
            for i, playlist_song in enumerate(playlist['items']):

                playlist_song_info.append({
                    "name": playlist_song['track']['name'],
                    "artist": playlist_song['track']['artists'][0]['name']
                })

            if playlist['next']:
                playlist = self.spotify_api.next(playlist)
            else:
                playlist = None

        return playlist_song_info