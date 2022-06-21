# Day 18 of Udemy's 100 Days of Python programming course
    # Code for extracting colours from image using colorgram
        # from tkinter import Y
        # import colorgram
        # colours = colorgram.extract("image.jpg", 10)

        # rgb_colours = []

        # for colour in colours:
        #     r = colour.rgb.r
        #     g = colour.rgb.g
        #     b = colour.rgb.b
        #     new_colour = (r, g, b)
        #     rgb_colours.append(new_colour)

        # print(rgb_colours)
import turtle as t
import random

screen = t.Screen()
pointer = t.Turtle()
pointer.penup()
pointer.hideturtle()
pointer.speed(0)
t.colormode(255)
colour_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68)]

y_pos = -500
pointer.setpos(-600, -500)

for rows in range(10):
    for columns in range(10):
        pointer.color(random.choice(colour_list))
        pointer.dot(40)
        pointer.fd(130)
    y_pos += 110
    pointer.setpos(-600, y_pos)
        
screen.exitonclick()