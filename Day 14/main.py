# Day 14 of Udemy's 100 Days of Python programming course
from game_data import data
from art import logo, vs
import random
import clear_function
from clear_function import clear

def get_random_account():
    """Returns a random account entry."""
    return random.choice(data)

def format_data(account):
    """Takes in an account entry and returns formatted data."""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}."

def check_answer(guess, a_followers, b_followers):
    """Takes in the user's guess and the follower counts of both account a and b, and returns the answer based on which has the higher follower count."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    """Plays the Higher-Lower game."""
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
        
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Whop has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if correct:
            score += 1
            print(f"You're correct! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's incorrect! Final score: {score}")

play_game()