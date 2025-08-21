import os
import sys
from googleapiclient.discovery import build

def force_utf8_stdio():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

def test_upcoming_streams():
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        channelId="UCvaTdHTWBGv3MKj3KVqJVCw",
        eventType="upcoming",
        type="video",
        maxResults=1
    )

    force_utf8_stdio()
    response = request.execute()

    items = response.get("items", [])
    if items:
        print("Upcoming stream title: ", items[0]["snippet"]["title"])
    else:
        print("No upcoming streams found.")
