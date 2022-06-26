# Day 23 of Udemy's 100 Days of Python programming course
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the scoreboard before updating it with refreshed level value."""
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def level_up(self):
        """Increase the level by one and updates the scoreboard to reflect this change."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Writes 'GAME OVER' to the centre of the screen."""
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
