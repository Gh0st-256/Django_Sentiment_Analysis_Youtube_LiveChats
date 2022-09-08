from django.shortcuts import render
from django.conf import settings
import requests


# Create your views here.

def index(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'part': 'snippet',
        'q': 'Sitting Parliament of Uganda',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 9
    }

    video_ids = []
    r = requests.get(search_url, params=params)
    print(r.json()['items'][0]['id']['videoId'])

    return render(request, 'index.html')
