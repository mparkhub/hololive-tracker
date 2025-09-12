from django.shortcuts import render
import os
from googleapiclient.discovery import build

def upcoming(request):
    api_key = os.getenv('YOUTUBE_API_KEY')

    youtube = build('youtube', 'v3', developerKey=api_key)

    request_api = youtube.search().list(
        part='snippet',
        channelId='UChAnqc_AY5_I3Px5dig3X1Q',
        eventType='upcoming',
        type='video',
        maxResults=1,
    )
    response=request_api.execute()

    items = response.get('items', [])
    streams = []
    for item in items:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        url = f'https://www.youtube.com/watch?v={video_id}'
        streams.append({'title':title, 'url':url})

    return render(request, 'streams/upcoming.html', {'streams': streams})
