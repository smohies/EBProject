from django.shortcuts import render
import requests

# temp key: will be a environment variable for production
key = "l7u502p8v46ba3ppgvj5y2aad50lb9"

# Create your views here.

def home(request):
    url = "https://api.stagingeb.com/v1/properties"
    usr = "X-Authorization"
    req = requests.get(url, headers={usr: key})
    data = req.json()

    pagination = data['pagination']

    content = data['content']

    context = {'content' : content}

    return render(request, 'ebproject/home.html', context)