# Day nine of Udemy's 100 Days of Python programming course
import clear_function
from clear_function import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}!")

while not bidding_finished:
    key = input("What is your name?: ")
    value = int(input("What is your bid?: "))
    bids[key] = value

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == "yes":
        clear()
    elif should_continue == "no":
        find_highest_bidder(bids)
        bidding_finished = True
