# Day 20 of Udemy's 100 Days of Python programming course
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Creates screen object, sets its dimensions, colour and title. Turns turtle animations off.
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialises the snake, intial food location and the scoreboard.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Begins listening to inputs. Changes direction using direction functions and Up/Down/Left/Right keys.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# If the snake head passes within 15 pixels of a food object, refresh food location, extend the snake and increase score.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detects collisions between the snake head and the bounds of the screen.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

# Detects collisions between the snake head and its proceeding segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()