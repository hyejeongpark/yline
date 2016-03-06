from django.shortcuts import render
from django.http import HttpResponse
import requests


def index_page(request):
    response = requests.get('https://www.googleapis.com/youtube/v3/search?part=id%2Csnippet&maxResults=25&q=dogs&key=AIzaSyAZCjuZgWCzKWQxTm7jRXe3TDWO3Hlu15M')
    context = {'items': response.json()['items']}
    return render(request, 'main/index.html', context)
