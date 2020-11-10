from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse
from .requests import get_all_ckan_list
from .requests import search_ckan


def index(request):
    return render(request, 'index.html', {})

def list_all(request):
    list_json = get_all_ckan_list()
    return HttpResponse(list_json)

def ckan_search(request):
    search_string = request.GET['q']
    response_json = search_ckan(search_string)
    return HttpResponse(response_json, content_type='application/json')