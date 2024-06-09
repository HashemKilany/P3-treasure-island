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

x = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'")
if x.lower() == "left":
    print(f"You have chosen {x.lower()}. You fell into a hole. Game Over")
elif x.lower() == "right":
    y = input(
        f"You have chosen {x.lower()}. You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if y.lower() == "swim":
        print(f"You have chosen {y.lower()}. You have been attacked by a trout. Game Over")
    elif y.lower() == "wait":
        z = input(
            "You have chosen {y.lower()}. You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if z.lower() == "red":
            print(f"You have chosen {z.lower()}. You have been burned by fire. Game Over")
        elif z.lower() == "blue":
            print(f"You have chosen {z.lower()}. You have been eaten by beasts. Game Over")
        elif z.lower() == "yellow":
            print(f"You have chosen {z.lower()}. You have found the treasure. You Win!")
