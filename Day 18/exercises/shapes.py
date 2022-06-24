# Day 18 of Udemy's 100 Days of Python programming course
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

tim.shape("turtle")

colours = ["SeaGreen", "SlateGray", "CornflowerBlue", "red", "orange", "black"]
num_sides = 3

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.fd(100)
        tim.rt(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


screen.exitonclick()