# Day 11 of Udemy's 100 Days of Python programming course
import random
from art import logo
import clear_function
from clear_function import clear


def deal_card():
    """Returns a random card from the card deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.choice(cards)]

def calculate_score(card_list):
    """Calculates the score of a provided list of cards and returns it."""
    for card in card_list:
        if sum(card_list) == 21 and len(card_list) == 2:
            return 0

        if sum(card_list) > 21 and 11 in card_list:
            card_list.remove(11)
            card_list.append(1)
    return sum(card_list)
 
def compare(user_score, computer_score):
    """Compares user score with computer score and returns a message based on the outcome."""
    if user_score > 21 and computer_score > 21:
        return "You lose! You went over."
    
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose. The computer has Blackjack!"
    elif user_score == 0:
        return "You win! you have a Blackjack!"
    elif user_score > 21:
        return "You lose! You went over!"
    elif computer_score > 21:
        return "You win! The computer went over!"
    elif user_score > computer_score:
        return "You win! Your score is higher!"
    else:
        return "You lose!" 



def play_blackjack():
    """Plays the Blackjack game."""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
            if choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play_blackjack()