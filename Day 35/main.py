# Day 35 of Udemy's 100 Days of Python programming course
import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "API KEY HERE"

account_sid = "ACCOUNT SIDE HERE"
auth_token = "AUTH TOKEN HERE"

weather_params = {
    "lat": "LAT HERE",
    "lon": "LON HERE",
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url = OWM_endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()

hourly_conditions = weather_data["hourly"][:12]

will_rain = False

for hour_data in hourly_conditions:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Bring an Umbrella!",
                     from_='FROM_NUMBER HERE',
                     to='TO_NUMBER HERE'
                 )

print(message.status)