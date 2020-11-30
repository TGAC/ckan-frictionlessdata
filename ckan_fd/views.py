from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse
from .requests import get_all_ckan_list
from .requests import search_ckan
from .requests import convert_ckan


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


def ckan_package_json(request):
    search_string = request.GET['q']
    response_json = convert_ckan(search_string)
    # return HttpResponse(response_json, content_type='application/json')
    filename = "datapackage.json"
    content = response_json
    response = HttpResponse(content, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response