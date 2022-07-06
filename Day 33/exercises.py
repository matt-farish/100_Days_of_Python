# Day 33 of Udemy's 100 Days of Python programming course
import requests

# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

response = requests.get(url = "https://api.kanye.rest")
response.raise_for_status()

data = response.json()

print(data)