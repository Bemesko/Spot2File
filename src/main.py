from utils.spotify_handler import SpotifyHandler
from utils.youtube_handler import YoutubeHandler


if __name__ == "__main__":
    spotify = SpotifyHandler()
    youtube = YoutubeHandler()

    playlist_file = open("playlist_links.txt", "r")

    for link in playlist_file:

        playlist_id = link.split("/")[-1]

        playlist_name = spotify.get_playlist_name(playlist_id)

        print(f"Downloading songs from {playlist_name}")

        songs = spotify.get_playlist_song_info(playlist_id)

        for song in songs:
            print(f"Searching for {song}...")
            search_query = song

            video_id = youtube.search_video(search_query)

            youtube.download_audio(video_id, playlist_name)

    print("Videos downloaded. Please check the output folder!")
