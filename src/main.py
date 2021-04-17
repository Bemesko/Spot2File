from utils.spotify_handler import SpotifyHandler
from utils.youtube_handler import YoutubeHandler
from youtube_dl import YoutubeDL


if __name__ == "__main__":

    audio_downloader = YoutubeDL(
        {"format": "bestaudio/best", 'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]})
    audio_downloader.download(
        ["https://www.youtube.com/watch?v=kZTxeeDyk1A"])

    spotify = SpotifyHandler()
    youtube = YoutubeHandler()

    # very cool playlist if anyone wants some city pop
    songs = spotify.get_playlist_song_info("2I1y0a2GYPdGHlUXW1JPwF")

    for song in songs:
        print(f"Searching for {song}...")
        search_query = song

        youtube.search_video(search_query)
