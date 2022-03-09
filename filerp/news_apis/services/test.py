import requests

from config.Config import API_KEY
from endpoints_everything.main import EndpointsEverything
from endpoints_sources.main import EndpointsSources


def print_response_json(response_data):
    data = []
    if response_data.json().get('endpoints_sources'):
        data = response_data.json().get('endpoints_sources')
    if response_data.json().get('articles'):
        data = response_data.json().get('articles')
    for item in data:
        print(item)


response = requests.get(EndpointsSources.get_sources_by_sports())
print_response_json(response)
response = requests.get(EndpointsEverything.with_keyword('South Africa'))
print_response_json(response)
