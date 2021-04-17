# Spot2File

A little script a made in order to convert my Spotify playlists to an mp3 format since I wanted to play them on my mp3 player.

## Usage

1. Copy and paste the links to all of the playlists you want to download in the `playlist_links.txt` file in the root directory
   1. Your links should look something like `https://open.spotify.com/playlist/XXXXXXXXXXXX`
   1. Make sure you paste only one link per line

## Installing this Repo

1. Open the command line, go into this project's root folder and create a virtual environment with `python -m venv venv`
1. Install the dependency libraries using `pip install -r requirements.txt`
1. Put your API keys in the file `src/utils/client_keys.py` (scroll down to see the file template)
   1. Get your Spotify API keys (follow [this link](https://developer.spotify.com/documentation/web-api/quick-start/)
   1. Get your Youtube Data API Key ([this article can explain better than me](https://blog.hubspot.com/website/how-to-get-youtube-api-key))
1. Make sure `ffmpeg` is installed (I found [this thread](https://stackoverflow.com/questions/30770155/ffprobe-or-avprobe-not-found-please-install-one) really useful for it)

### API File Template

```python
CLIENT_ID = 'Your Spotify ID'
CLIENT_SECRET = 'Your Spotify Secret ID'
YOUTUBE_API_KEY = 'Your YouTube Data API Key'
```

## Feature Checklist

- [x] Read a Spotify playlist link from a file
- [x] Connect to Spotify and retrieve the name of every song in the playlist
- [x] Search the internet for a link of each song
- [x] Download the song and put it in a folder with the playlist's name
- [ ] Keep song metadata with mp3
