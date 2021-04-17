from utils.spotify_handler import SpotifyHandler
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import utils.client_keys as client_keys


def youtube_search(search):

    youtube = build('youtube', 'v3', developerKey=client_keys.YOUTUBE_API_KEY)

    search_response = youtube.search().list(
        q=search,
        part="id,snippet",
        maxResults=2
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))
    print("Videos:\n", "\n".join(videos), "\n")


if __name__ == "__main__":
    spotify = SpotifyHandler()
    songs = spotify.get_playlist_song_info("2I1y0a2GYPdGHlUXW1JPwF") # very cool playlist if anyone wants some city pop

    for song in songs:
        search_query = song
        try:
            youtube_search(search_query)
        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" %
                  (e.resp.status, e.content))
