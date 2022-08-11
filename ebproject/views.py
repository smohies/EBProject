from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    url = "https://api.stagingeb.com/v1/properties"
    usr = "X-Authorization"
    key = "l7u502p8v46ba3ppgvj5y2aad50lb9"
    headers = {usr: key}
    payload = {"page":1, "limit":15, "search[statuses][]":"published"}
    req = requests.get(url, headers=headers, params=payload)
    data = req.json()

    pagination = data['pagination']

    content = data['content']

    context = {'content' : content}

    return render(request, 'ebproject/home.html', context)