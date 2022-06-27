# Day 21 of Udemy's 100 Days of Python programming course
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            high_score = int(file.read())
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes the scoreboard onto the screen."""
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        """Increases the score by 1, clears the old scoreboard and updates with the new score."""
        self.score += 1 
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
