from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import urljoin
import requests
from .forms import InputForm
from .token_auth import TokenAuth

def home(request, value=1):
    url = urljoin(settings.EB_BASE_URL, settings.EB_PROPERTIES_ENDPOINT)
    payload = {"page": value, "limit": settings.PROPERTIES_PAGE_SIZE_LIMIT, "search[statuses][]": "published"}
    res = requests.get(url, auth=TokenAuth(settings.API_KEY), params=payload)
    data = res.json()

    pagination = data['pagination']
    content = data['content']

    # Add the total of pages available to pagination.
    pagination["pages"] = pagination["total"] // pagination["limit"]
    if pagination["total"] % pagination["limit"]:
        pagination["pages"] += 1

    # Create a 1-based list of pages available.
    pages = [n+1 for n in range(pagination["pages"])]

    # Add a generic thumbnail to properties with a null thumbnail.
    for count in range(len(content)):
        if not content[count]["title_image_thumb"]:
            content[count]["title_image_thumb"] = "https://www.komar.de/en/media/catalog/product/cache/5/image/100x100/17f82f742ffe127f42dca9de82fb58b1/6/0/6041a-vd2_blue_sky_web.jpg"

    context = {'eb_properties': content, 'pagination': pagination, 'pages': pages}

    return render(request, 'ebproject/home.html', context)

def properties(request, property_id):
    url = urljoin(settings.EB_BASE_URL, settings.EB_PROPERTIES_ENDPOINT + f"/{property_id}")
    res = requests.get(url, auth=TokenAuth(settings.API_KEY))
    data = res.json()

    # Create a dictionary with the property image urls
    # if less than 3, repeat until 3, if none, add 3 generic images.
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

    context = {'data': data, 'images': images,
               'form': InputForm(initial={'public_id': property_id})}

    return render(request, 'ebproject/property.html', context)

def leads(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = {
                "name": form.cleaned_data["name"],
                "phone": form.cleaned_data["phone"],
                "email": form.cleaned_data["email"],
                "property_id": form.cleaned_data["public_id"],
                "message": form.cleaned_data["message"],
                "source": "mydomain.com"
            }

            url = urljoin(settings.EB_BASE_URL, settings.EB_CONTACT_ENDPOINT) 
            req = requests.post(url, auth=TokenAuth(settings.API_KEY), json=data)
            response = req.status_code
            context = {'data': data, 'response':response}
            if response == 200:
                return render(request, 'ebproject/lead.html', context)

            return HttpResponse("Error code: " + str(response))

        return HttpResponse("Form is not valid")     