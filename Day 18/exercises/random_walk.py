# Day 18 of Udemy's 100 Days of Python programming course
import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

tim.shape("classic")
tim.pensize(15)
tim.speed("fastest")
directions = [0, 90, 180, 270]

def move():
    """Makes the turtle move, then randomly change direction and colour."""
    tim.fd(50)
    tim.setheading(random.choice(directions))
    tim.color(random_colour())

for i in range(200):
    move()

screen.exitonclick()