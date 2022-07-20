#Day 45 of Udemy's 100 Days of Python programming course
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

films = soup.findAll(name = "h3", class_ = "title")

film_list = [film.getText() for film in films]


film_list.reverse()

with open("movies.txt", mode = "w", encoding = "utf-8") as file:
    for film in film_list:
        file.write(f"{film}\n")