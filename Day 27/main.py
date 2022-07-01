# Day 27 of Udemy's 100 Days of Python programming course
from tkinter import *

def miles_to_km():
    """Converts miles to KM by taking the value from an input and formatting the answer using the result."""
    miles = float(input.get())
    km = miles * 1.609
    answer.config(text = f"{km}")

# Creates a window, sets its title and adds padding to the window.
window = Tk()
window.title("Miles to KM converter")
window.config(padx = 20, pady = 20)

# Creates a global tuple containing the values to alter the font of an element.
FONT = ("Arial", 24, "bold")

# Creates an input box.
input = Entry(width = 5)
input.grid(column = 1, row = 0)

# Creates a label called miles.
miles = Label(text = "Miles", font = FONT)
miles.grid(column = 2, row = 0)

# Creates a label that displays "is equal to".
is_equal_to = Label(text = "is equal to", font = FONT)
is_equal_to.grid(column = 0, row = 1)

# Creates a label the display the answer.
answer = Label(text = "0", font = FONT)
answer.grid(column = 1, row = 1)

# Creates a label that displays "KM"
km = Label(text = "KM", font = FONT)
km.grid(column = 2, row = 1)

# Creates a button used to calculate the answer and display it.
button = Button(text = "Calculate", command = miles_to_km)
button.grid(column = 1, row = 2)

# Keeps the window open.
window.mainloop()