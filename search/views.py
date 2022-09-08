from django.shortcuts import render
from django.conf import settings
import requests


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
        print(result['id']['videoId'])

    video_params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet',
        'id': ','.join(video_ids)

    }

    r = requests.get(video_url, params=video_params)

    print(r.text)

    return render(request, 'index.html')
