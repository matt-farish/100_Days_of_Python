# Day 33 of Udemy's 100 Days of Python programming course

from datetime import datetime
import requests


MY_LAT = -38.182968
MY_LONG = 145.090591

parameters = {
    "late": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)