# Day three of Udemy's 100 Days of Python programming course
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
answer1 = input("You wake in a room filled with cobwebs. There are two doors on either side of the room. Do you go left or right?\n").lower()
if answer1 == "left":
    answer2 = input("You open the door to find a lush open area with a large lake. At the centre, is an island. Do you wait for a boat to arrive or swim across? (Type either 'wait' or 'swim')\n").lower()
    if answer2 == "wait":
        answer3 = input("You make it to the island, to a find a house with three coloured doors: Red, Yellow and Blue. Which colour door do you open? \n").lower()
        if answer3 == "red":
            print("You open the door and an explosive fireball consumes you. You have died.")
        elif answer3 == "blue":
            print("You open the door and are immediately swarmed by large blue beetles. They eat you alive. You have died.")
        elif answer3 == "yellow":
            print("You open the door to find a massive wooden chest filled with gold. You win!")
        else:
            print("You chose a door colour that doesn't exist. The house explodes. You have died.")
    else:
        print("You enter the water and feel sharp pains in your feet. Piranhas latch on to you all at once. You have died.")
else:
    print("You open the door and step through, immediately falling into a deep hole. You have died.")