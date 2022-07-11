# Day 37 of Udemy's 100 Days of Python programming course
import requests
from datetime import datetime

USERNAME = "USERNAME HERE"
TOKEN = "TOKEN HERE"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Days",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year = 2022, month = 7, day = 9)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

# response = requests.post(url = pixel_endpoint, json = pixel_config, headers = headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220708"

pixel_update_config = {
    "quantity": "1"
}
response = requests.put(url = update_endpoint, json = pixel_update_config, headers = headers)
print(response.text)
