# Day 15 of Udemy's 100 Days of Python programming course
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def valid_resources(order_ingredients):
    """Checks to see if their are enough resources remaining to make the drink chosen."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def check_coins():
    """Prompts for coins to be inserted and returns the total value of the coins inserted."""
    print("Insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total 

def check_transaction(money_received, drink_cost):
    """Checks the transaction based on the money received and the cost of the drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Thanks, here is ${change} in change!")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded below.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Removes the appropriate amount of resources based on the drink selected, and prints a message stating the drink has been made."""
    for item in order_ingredients:
        resources[item] - order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/ latte/ cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profits: ${profit}")
    else:
        drink = MENU[choice]
        if valid_resources(drink["ingredients"]):
            payment = check_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])