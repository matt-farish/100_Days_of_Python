# Day 28 of Udemy's 100 Days of Python programming course
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Resets the timer. Sets timer text and title label back to default. Clears checkmarks and sets
    reps back to 0."""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    checkmark.config("")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """Starts the timer, increases reps and checks to see what rep the timer is at, adjusting the
    title label accordingly."""
# Takes in reps and adds 1 to it.
    global reps
    reps += 1
# Variables for the length of time for each variation of timer. (A working timer, a short break timer 
# and a long break timer.)
    work_sec = WORK_MIN * 60
    short_break__sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
# If the number of reps is 8, commence a long break timer.
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "Break", fg = RED)
# If the number of reps is even (In between working periods), commence a short break timer.
    elif reps % 2 == 0:
        count_down(short_break__sec)
        title_label.config(text = "Break", fg = PINK)
# If the number of reps is odd (A working period), commence a working timer.
    else:
        count_down(work_sec)
        title_label.config(text = "Work", fg = GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """Counts down by one second, adjusting the timer text to display the current minutes and seconds."""
# Takes in the count provided and creates variables to account for the number of minutes and seconds.
    count_min = math.floor(count / 60)
    count_sec = count % 60
# If the number of seconds is less than 10, print a 0 in front of the second value, to retain correct
# formatting of the timer.
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
# If count isn't 0, begin counting down by one second.
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
# When the count reaches zero, start the timer again and calculate the number of work sessions conducted.
# For the number of work sessions conducted, add another checkmark.
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text = marks)



# ---------------------------- UI SETUP ------------------------------- #

# Creates a window, sets its title and changes the padding and background colour.
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# Creates all the elements in the window and positions them in the grid. 
title_label = Label(text = "Timer", font = (FONT_NAME, 45, "bold"), bg = YELLOW, fg = GREEN)
title_label.grid(row = 0, column = 1)

start = Button(text = "Start", font = (FONT_NAME), relief = "groove", command = start_timer)
start.grid(row = 2, column = 0)

reset = Button(text = "Reset", font = (FONT_NAME), relief = "groove", command = reset_timer)
reset.grid(row = 2, column = 2)

checkmark = Label(text = "", font = (FONT_NAME, 15), fg = GREEN, bg = YELLOW)
checkmark.grid(row = 3, column = 1)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)

timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

# Keeps the window open.
window.mainloop()