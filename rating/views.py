from django.shortcuts import render
import requests
import json

# Create your views here.
# def home(request):
# #view to retrieve data from the awwwards api
#     url = 'https://www.awwwards.com/api/annual/categories?page=1'

#     response = requests.get(url)

#     content = response.json()


#     return render(request, 'home.html', {'data': content})

def get_data(self,api):
    url = 'https://www.awwwards.com/api/annual/categories?page=1'
    response = requests.get(url)
    content = response.json()
    return content


def home(request):
    data = get_data(request, 'https://www.awwwards.com/api/annual/categories?page=1')
    return render(request, 'home.html', {'data': data})
