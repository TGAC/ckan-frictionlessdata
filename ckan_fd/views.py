from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import requests
import re
import json

# Create your views here.

from django.http import HttpResponse
from .requests import get_all_ckan_list
from .requests import search_ckan
from .requests import convert_ckan
from .requests import convert_ckan_resources
from .requests import push_to_ckan


def index(request):
    # list_json = get_all_ckan_list()
    # return render(request, 'index.html', {'data': json.dumps(list_json.get('result'))})
    return render(request, 'index.html', {})


def list_all(request):
    list_json = get_all_ckan_list()
    return HttpResponse(list_json)


def ckan_search(request):
    search_string = request.GET['q']
    response_json = search_ckan(search_string)
    return HttpResponse(response_json, content_type='application/json')


def ckan_convert(request):
    search_string = request.GET['q']
    response_json = convert_ckan(search_string)
    return HttpResponse(response_json, content_type='application/json')


def ckan_convert_resources(request):
    search_string = request.GET['q']
    response_json = convert_ckan_resources(search_string)
    return HttpResponse(response_json, content_type='application/json')


def ckan_package_json(request):
    search_string = request.GET['q']
    response_json = convert_ckan(search_string)
    # return HttpResponse(response_json, content_type='application/json')
    filename = "datapackage.json"
    content = response_json
    response = HttpResponse(content, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response


def ckan_convert_push(request):
    search_string = request.GET['q']
    ckan_key = request.GET['key']
    response_json = convert_ckan_resources(search_string)
    response = push_to_ckan(search_string, ckan_key, response_json)
    return HttpResponse(response, content_type='application/json')

