
import requests, json
import os
import time
import requests


# File must be in the same directory 
def postRequest(filename):
    data = {
    'api_token': '53974634fb430490fdbbf8254b2964aa',
    'return': 'apple_music,spotify',
    }
    files = {
        'file': open(filename, 'rb'),
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    data = json.loads(result.text)
    return data["result"]["artist"], data["result"]["title"]