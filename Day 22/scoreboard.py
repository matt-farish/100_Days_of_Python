# Day 22 of Udemy's 100 Days of Python programming course
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        """Creates a scoreboard with scores for both players. Clears old score on every call."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Adds a point to the left player's score."""
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        """Adds a point the right player's score."""
        self.r_score += 1
        self.update_scoreboard()