import json
import pprint
import requests


def get_events():
    r = requests.get('https://reqres.in/api/users')
    json_data = json.loads(r.text)
    pprint.pprint(json_data)
