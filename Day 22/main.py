# Day 22 of Udemy's 100 Days of Python programming course
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Creates screen object, sets its dimensions, colour and title. Turns turtle animations off.
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Initialises the left and right paddles, ball, and scoreboard.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Begins listening for inputs. Changes direction of the paddles using the go_up and go_down functions, based on
# the keys pressed.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# If the ball hits either the top or bottom wall, call the bounce function.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# If the ball comes within a certain distance of a paddle and the ball hasn't already passed the paddle, call
# the bounce function.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# If the ball passes by the right paddle, reset the ball's position and add a point to the left player's score.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

# If the ball passes by the left paddle, reset the ball's position and add a point to the right player's score.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()