import requests

name = input("Enter a name: ")

gender_url = f"https://api.genderize.io?name={name}"

gender_response = requests.get(gender_url)
gender_data = gender_response.json()
gender = gender_data["gender"]


age_url = f"https://api.agify.io?name={name}"

age_response = requests.get(age_url)
age_data = age_response.json()
age = age_data["age"]

print(f"Hi {name.title()}.\nI guess you are {age} years old.\nI guess you are {gender}")