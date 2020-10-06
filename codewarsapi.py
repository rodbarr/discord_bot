import json
import requests

API_TOKEN = "?access_key=V93QtNVwDczdWg24u29"
URL = "https://www.codewars.com/api/v1/users/"

user = input("Enter the user you want to look for: ")

a = requests.get(f"{URL}{user}{API_TOKEN}")
data = a.json()

print(data['name'], data['honor'])
