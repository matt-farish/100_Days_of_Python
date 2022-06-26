# Day 23 of Udemy's 100 Days of Python programming course
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def is_at_finish_line(self):
        """Checks to see if the player object is at or past the finish line."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def move(self):
        """Moves the player forward."""
        self.fd(MOVE_DISTANCE)

    def reset(self):
        """Sets the player back to the starting position."""
        self.goto(STARTING_POSITION)
