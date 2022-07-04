# Day 31 of Udemy's 100 Days of Python programming course
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text = "French", fill = "Black")
    canvas.itemconfig(word_text, text = current_card["French"], fill = "Black")
    canvas.itemconfig(canvas_image, image = card_front_image)
    window.after(3000, flip_card)



def flip_card():
    canvas.itemconfig(canvas_image, image = card_back_image)
    canvas.itemconfig(language_text, text = "English", fill = "White")
    canvas.itemconfig(word_text, text = current_card["English"], fill = "White")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file = "images/card_back.png")
canvas_image = canvas.create_image(400, 263, image = card_front_image)
language_text = canvas.create_text(400, 150, text = "Language", font = ("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

unknown_image = PhotoImage(file = "images/wrong.png")
unknown_button = Button(image = unknown_image, relief = "groove", highlightthickness = 0, borderwidth = 0, command = next_card)
unknown_button.grid(row = 1, column = 0)

check_image = PhotoImage(file = "images/right.png")
check_button = Button(image = check_image, relief = "groove", highlightthickness = 0, borderwidth = 0, command = is_known)
check_button.grid(row = 1, column = 1)

# ---------------------------- EXECUTION ------------------------------- #
flip_timer = window.after(3000, flip_card)

next_card()

window.mainloop()