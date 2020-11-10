import requests
import json

server_url = "https://ckan.grassroots.tools/api/3/action/package_search?q="

def get_all_ckan_list():
    res = requests.get(server_url)
    return json.dumps(res.json())

def search_ckan(string):
    res = requests.get(server_url+string)
    return json.dumps(res.json())