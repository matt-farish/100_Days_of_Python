# Day 23 of Udemy's 100 Days of Python programming course
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creates screen object and sets its dimensions. Turns turtle animations off.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialises the player, scoreboard and car manager.
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Begins listening for inputs. Moves the player if the Up key is pressed.
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_cars()

# If the player is at the finish line, reset their position, increase the level by one and increase the speed of
# the cars.
    if player.is_at_finish_line():
        player.reset()
        scoreboard.level_up()
        car_manager.increase_difficulty()

# Fore every car on the screen, if the player is within a certain distance, game over is display and the game ends.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
