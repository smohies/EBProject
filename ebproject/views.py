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
    
    # add thumbnail to properties with a null thumbnail
    for count in range(len(content)):
        if not content[count]["title_image_thumb"]:
            content[count]["title_image_thumb"] = "https://www.komar.de/en/media/catalog/product/cache/5/image/100x100/17f82f742ffe127f42dca9de82fb58b1/6/0/6041a-vd2_blue_sky_web.jpg"

    context = {'content' : content}

    return render(request, 'ebproject/home.html', context)

def properties(request, value):
    url = f"https://api.stagingeb.com/v1/properties/{value}"
    usr = "X-Authorization"
    key = "l7u502p8v46ba3ppgvj5y2aad50lb9"
    headers = {usr: key}
    req = requests.get(url, headers=headers)

    data = req.json()

    # create a dic with the prop imgs, if less than 3, repeat imgs until 3, if none, add generic images
    images = {}
    if len(data["property_images"]) > 0:
        for count, image in enumerate(data["property_images"]):
            images[count] = image["url"]
        if 1 not in images:
            images[1] = images[0]
        if 2 not in images:
            images[2] = images[0]
    else:
        for count in range(3):
            images[count] = "http://wallpaperswide.com/download/sky_hd-wallpaper-1920x1080.jpg"

    context = {'data':data,'images':images}

    return render(request, 'ebproject/property.html', context)