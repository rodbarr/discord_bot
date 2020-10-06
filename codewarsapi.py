import json
import requests
import config

def getUser(user):
    a = requests.get(f"{config.URL}{user}{config.API_TOKEN}")
    data = a.json()
    return data