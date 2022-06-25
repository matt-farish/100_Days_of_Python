# Day 21 of Udemy's 100 Days of Python programming course
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes the scoreboard onto the screen."""
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        """Increases the score by 1, clears the old scoreboard and updates with the new score."""
        self.score += 1 
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Writes game over onto the screen."""
        self.goto(0, 0)
        self.write("Game Over!", align = ALIGNMENT, font = FONT)