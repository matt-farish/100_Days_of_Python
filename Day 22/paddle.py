# Day 22 of Udemy's 100 Days of Python programming course

from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        """Sets a new y coordinate, and moves the paddle up, as long as the new y value is less than 250."""
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Sets a new y coordinate, and moves the paddle down, as long as the new y value is more than -250."""
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)