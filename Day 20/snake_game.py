# Day 20 of Udemy's 100 Days of Python programming course
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(position)
    segments.append(snake_segment)

screen.update()

game_is_on = True

while game_is_on:
    for segment in segments:
        segment.forward(20)




screen.exitonclick()