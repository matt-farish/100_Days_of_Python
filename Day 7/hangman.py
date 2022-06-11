# Day seven of Udemy's 100 Days of Python programming course
import random
# Imports the clear function, for clearing the screen after each guess.
import clear_function
from clear_function import clear

from hangman_art import stages, logo
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(logo)

#print(f'Pssst, the solution is {chosen_word}.')
display = []
for letter in chosen_word:
    display += "_"

print(logo)
while not end_of_game:
    guess = input("Enter your guess: ").lower()
    clear()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
        
    if guess not in chosen_word:
        print("You guessed a letter that isn't in the word!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    [print(stages[lives])]
