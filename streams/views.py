from django.shortcuts import render
import os
from googleapiclient.discovery import build

def upcoming(request):
    api_key = os.getenv('YOUTUBE_API_KEY')

    youtube = build('youtube', 'v3', developerKey=api_key)

    channel_ids = [
        'UCvaTdHTWBGv3MKj3KVqJVCw',     # Nekomata Okayu
        'UChAnqc_AY5_I3Px5dig3X1Q',     # Inugami Korone
        'UCp-5t9SrOQwXMU7iIjQfARg',     # Ookami Mio
        'UCdn5BQ06XqgXoAxIhbqw5Rg'      # Shirakami Fubuki
    ]

    upcoming_streams = []

    for cid in channel_ids:
        request_api = youtube.search().list(
            part='snippet',
            channelId=cid,
            eventType='upcoming',
            type='video',
            maxResults=1,
        )
        response=request_api.execute()
        upcoming_streams.extend(response.get('items', []))

    streams = []
    for stream in upcoming_streams:
        title = stream['snippet']['title']
        video_id = stream['id']['videoId']
        url = f'https://www.youtube.com/watch?v={video_id}'
        streams.append({'title':title, 'url':url})

    return render(request, 'streams/upcoming.html', {'streams': streams})
