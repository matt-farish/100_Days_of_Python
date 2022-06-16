# Day 12 of Udemy's 100 Days of Python programming course
from random import randint
from art import logo
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5


def difficulty_select():
    """Allows the user to choose between Easy or Hard difficulty, returning a value to be used as the number of attempts."""
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_MODE_ATTEMPTS
    elif difficulty == 'hard':
        return HARD_MODE_ATTEMPTS

def guess_check(guess, number):
    """Checks the provided guess to see if it is too high, or too low."""
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")

def play_number_guess():
    """Plays the number guess game."""
    guess = 0
    number = randint(1, 100)

    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = difficulty_select()
    
    while guess != number and attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        guess_check(guess, number)
        attempts -= 1
        if guess != number and attempts == 0:
            print(f"You ran out of guesses. You lose! The number was {number}.")
        elif guess == number:
            print(f"You guessed it! The number was {number}.")
    
play_number_guess()