from utils.client_keys import YOUTUBE_API_KEY
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YoutubeHandler():

    def __init__(self) -> None:
        self.youtube_api = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    def search_video(self, search):
        try:
            search_response = self.youtube_api.search().list(
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
        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" %
                  (e.resp.status, e.content))
