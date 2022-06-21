# Day 18 of Udemy's 100 Days of Python programming course
import turtle as turtle_module
import random

tim = turtle_module.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
colour_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68)]
turtle_module.colormode(255)

tim.setheading(225)
tim.fd(400)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = turtle_module.Screen()

screen.exitonclick()