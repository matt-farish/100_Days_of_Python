# Day 19 of Udemy's 100 Days of Python programming course
from re import L
from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()

def move_forwards():
    pointer.fd(10)

def move_backwards():
    pointer.bk(10)

def clockwise():
    pointer.right(10)

def counter_clockwise():
    pointer.left(10)

def reset():
    pointer.reset()


screen.listen()

screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = reset)

screen.exitonclick()