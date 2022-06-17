# Day 14 of Udemy's 100 Days of Python programming course
from game_data import data
from art import logo, vs
import random
import clear_function
from clear_function import clear

def get_random_account():
    return random.choice(data)

