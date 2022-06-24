# Day 18 of Udemy's 100 Days of Python programming course
import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed(0)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

def spirograph(gap_size):
    for i in range(int(360/ gap_size)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

spirograph(3)

screen.exitonclick()