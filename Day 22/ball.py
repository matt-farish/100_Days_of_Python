# Day 22 of Udemy's 100 Days of Python programming course
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Sets locations for the ball to move to, before issuing a command to move to said locations."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Inverts the y_move number, causing the ball to change directions on the y-axis."""
        self.y_move *= -1

    def bounce_x(self):
        """Inverts the x_move number, causing the ball to change directions on the x-axis. Adjusts the ball's speed 
        upon contact with a paddle."""
        self.x_move *= -1
        self.move_speed * 0.9

    def reset_position(self):
        """Resets the ball's position, changes its speed back to the original value and changes its direction on
        the x-axis"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
    