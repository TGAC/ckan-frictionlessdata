import requests
import json
import csv
from contextlib import closing
from frictionless_ckan_mapper import ckan_to_frictionless

search_url = "https://ckan.grassroots.tools/api/3/action/package_search?q="

list_url = "https://ckan.grassroots.tools/api/3/action/package_list"

detail_url = "https://ckan.grassroots.tools/api/3/action/package_show?id="

resource_create_url = "https://ckan.grassroots.tools/api/3/action/resource_create"

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
    output_frictionless_dict = ckan_to_frictionless.dataset(res_json.get('result'))
    return json.dumps(output_frictionless_dict)

def convert_ckan_resources(string):
    res = requests.get(detail_url+string)
    res_json = res.json()
    output_frictionless_dict = ckan_to_frictionless.resource(res_json.get('result'))
    csv_resource = csv_datapackage(output_frictionless_dict)
    return json.dumps(csv_resource)

def csv_datapackage(output_frictionless_dict):
    for resource in output_frictionless_dict['resources']:
        if resource['format'] == 'CSV':
            # file_content = requests.get(resource['url'])
            schema = generate_csv_schema(resource['url'])
            resource['schema'] = schema
    return output_frictionless_dict


def generate_csv_schema(url):
    r = requests.get(url)
    decoded_content = r.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    d = {}
    field = []
    for element in my_list[0]:
        element_json = {}
        element_json['name'] = element
        element_json['type'] = 'string'
        field.append(element_json)
    d['field'] = field
    return d


def push_to_ckan(entry_id, key, file_content):
    response = requests.post(resource_create_url,
                  data={"package_id": entry_id, "name":"datapackage.json"},
                  headers={"X-CKAN-API-Key": key},
                  files=[('upload', file_content)])
    return response