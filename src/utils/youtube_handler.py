from utils.client_keys import YOUTUBE_API_KEY
from youtube_dl import YoutubeDL
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YoutubeHandler():

    def __init__(self) -> None:
        self.youtube_api = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    def search_video(self, search):
        try:
            search_response = self.youtube_api.search().list(
                q=search,
                part="id",
                maxResults=1
            ).execute()

            search_result = search_response.get("items", [])[0]

            if search_result["id"]["kind"] == "youtube#video":
                return search_result["id"]["videoId"]

        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" %
                  (e.resp.status, e.content))

    def download_audio(self, video_id, playlist_name):
        self.audio_downloader = YoutubeDL(
            {"format": "bestaudio/best",
             'outtmpl': f'output/{playlist_name}/%(title)s.%(ext)s',
             'postprocessors': [{
                 'key': 'FFmpegExtractAudio',
                 'preferredcodec': 'mp3',
                 'preferredquality': '192'
             }]})

        self.audio_downloader.download(
            [f"https://www.youtube.com/watch?v={video_id}"])
