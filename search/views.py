from django.shortcuts import render
from django.conf import settings
import requests
from isodate import parse_duration


# Create your views here.

def index(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
        'part': 'snippet',
        'q': 'Sitting Parliament of Uganda',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 9,
        'type': 'video'
    }

    video_ids = []
    r = requests.get(search_url, params=search_params)

    results = r.json()['items']

    for result in results:
        video_ids.append(result['id']['videoId'])

    video_params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet, contentDetails',
        'maxResults': 9,
        'id': ','.join(video_ids)

    }

    r = requests.get(video_url, params=video_params)

    results = (r.json()['items'])

    videos = []
    for result in results:
        video_data = {
            'title': result['snippet']['title'],
            'id': result['id'],
            'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail': result['snippet']['thumbnails']['high']['url']
        }
        videos.append(video_data)

    context = {
        'videos': videos

    }

    return render(request, 'index.html', context)
