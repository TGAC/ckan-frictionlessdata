import requests
import json
from frictionless_ckan_mapper import ckan_to_frictionless

search_url = "https://ckan.grassroots.tools/api/3/action/package_search?q="

list_url = "https://ckan.grassroots.tools/api/3/action/package_list"

detail_url = "https://ckan.grassroots.tools/api/3/action/package_show?id="

#0c03fa08-2142-426b-b1ca-fa852f909aa6

def get_all_ckan_list():
    res = requests.get(list_url)
    return json.dumps(res.json())

def search_ckan(string):
    res = requests.get(search_url+string)
    return json.dumps(res.json())

def convert_ckan(string):
    res = requests.get(detail_url+string)
    res_json = res.json()
    output_frictionless_dict = ckan_to_frictionless.resource(res_json.get('result'))
    return json.dumps(output_frictionless_dict)