#Day 55 of Udemy's 100 Days of Python programming course
from flask import Flask
import random

number = random.randint(0, 9)
print(number)

app = Flask(__name__)

@app.route("/")
def higher_lower():
    return "<h1>Guess a number between 0 and 9.</h1>\
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return "<h1 style='color: red'>Too High!</h1>\
            <img src='https://i.pinimg.com/originals/25/2e/4c/252e4c91304826da1ab9c5e41a13d83d.png'/>"
    elif guess < number:
        return "<h1 style='color: blue'>Too Low!</1h1>\
            <img src='https://www.pngitem.com/pimgs/m/200-2002544_emoji-face-cold-freezing-hd-png-download.png' width = 200 heigth = 200/>"
    else:
        return "<h1 style='color: green'>You got it!</h1>\
            <img src='https://image.emojisky.com/358/2212358-middle.png'/>"

if __name__ == "__main__":
    app.run(debug=True)