from utils.spotify_handler import SpotifyHandler
from utils.youtube_handler import YoutubeHandler


if __name__ == "__main__":
    spotify = SpotifyHandler()
    youtube = YoutubeHandler()

    # very cool playlist if anyone wants some city pop
    songs = spotify.get_playlist_song_info("2I1y0a2GYPdGHlUXW1JPwF")

    for song in songs:
        search_query = song

        youtube.search_video(search_query)
