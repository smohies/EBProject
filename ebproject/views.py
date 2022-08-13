from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import math
from urllib.parse import urljoin
import requests
from .forms import InputForm
from .token_auth import TokenAuth

def home(request, value=1):
    url = urljoin(settings.EB_BASE_URL, settings.EB_PROPERTIES_ENDPOINT)
    payload = {"page": value, "limit": settings.PROPERTIES_PAGE_SIZE_LIMIT, "search[statuses][]": "published"}
    res = requests.get(url, auth=TokenAuth(settings.API_KEY), params=payload)

    data = res.json()
    response_pagination = data['pagination']
    response_content = data['content']
    total_pages = math.ceil(response_pagination['total'] / response_pagination['limit'])

    pagination = {
        "page": response_pagination['page'],
        "total_pages": total_pages,
        "page_list": range(1, total_pages+1)
    }

    context = {'eb_properties': response_content, 'pagination': pagination}

    return render(request, 'ebproject/home.html', context)

def properties(request, property_id):
    url = urljoin(settings.EB_BASE_URL, settings.EB_PROPERTIES_ENDPOINT + f"/{property_id}")
    res = requests.get(url, auth=TokenAuth(settings.API_KEY))
    data = res.json()
    
    context = {'data': data, 'slider': range(len(data["property_images"])),
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
            res = requests.post(url, auth=TokenAuth(settings.API_KEY), json=data)
            response = res.status_code
            context = {'data': data, 'response':response}
            if response == 200:
                return render(request, 'ebproject/lead.html', context)

            return HttpResponse("Error code: " + str(response), status = response)

        return HttpResponse("Form is not valid", status = 400)     