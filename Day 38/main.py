# Day 38 of Udemy's 100 Days of Python programming course
import requests
from datetime import datetime
import os
from decouple import config

APP_ID = config("APP_ID")
API_KEY = config("API_KEY")

exercise_tracking_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("What exercise did you do today? ")

user_params = {
    "query": query
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY 
}

response = requests.post(url = exercise_tracking_endpoint, json = user_params, headers = headers)
exercise_data = response.json()

sheety_endpoint = "https://api.sheety.co/7daa6c5959688edcd92405afffeb16fc/myWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_header = {
    "Authorization": config("BEARER_ID")
}

for exercise in exercise_data["exercises"]:
    sheety_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json = sheety_input, headers = bearer_header)

    print(sheety_response.text)