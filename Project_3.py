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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("You are at a cross road where do you want to go; type right or left: ")
if choice1.lower() == "left":
    print("Great choice")
    choice2 = input("What do you want to do; type swim or wait: ")
    if choice2.lower() == "wait":
        print("Great choice")
        choice3 = input ("Which door do wanna open; type red , blue or yellow: ")
        if (choice3.lower() == "yellow"):
            print(">>Congratulatons!!")
            print(">>You have won the game!!")
        elif (choice3 == "red"):
            print("Wrong Choice")
            print("Game Over")
        else:
            print("Wrong choice")
            print("Game Over")         


    else:
        print("Wrong Choice")
        print("Game Over")   


else:
    print("Game Over")
