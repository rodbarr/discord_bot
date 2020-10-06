import json
import requests

API_TOKEN = "?access_key=some_api_Key"
URL = "https://www.codewars.com/api/v1/users/"

user = input("Enter the user you want to look for: ")

a = requests.get(f"{URL}{user}{API_TOKEN}")
data = a.json()

print(data['name'], data['honor'])


# def getUser(user):
#     a = requests.get(f"{URL}{user}{API_TOKEN}")
#     data = a.json()
#     return data
