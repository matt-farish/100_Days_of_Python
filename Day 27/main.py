# Day 27 of Udemy's 100 Days of Python programming course
from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    answer.config(text = f"{km}")

window = Tk()
window.title("Miles to KM converter")
window.config(padx = 20, pady = 20)
FONT = ("Arial", 24, "bold")

input = Entry(width = 5)
input.grid(column = 1, row = 0)

miles = Label(text = "Miles", font = FONT)
miles.grid(column = 2, row = 0)

is_equal_to = Label(text = "is equal to", font = FONT)
is_equal_to.grid(column = 0, row = 1)

answer = Label(text = "0", font = FONT)
answer.grid(column = 1, row = 1)

km = Label(text = "KM", font = FONT)
km.grid(column = 2, row = 1)

button = Button(text = "Calculate", command = miles_to_km)
button.grid(column = 1, row = 2)


window.mainloop()