# Snake Water Gun
'''
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
'''

import random
# user win -> - 1, comp win -> +1
def check(user, comp):
    if user == comp:
        return 0
    elif user == 0 and comp == 1:
        return -1 
    elif user == 0 and comp == 2:
        return -1
    else:
        return 1

while True:
    comp = random.randint(0,2)
    print("---------------------- ")
    print("0 for Snake\n1 for Water\n2 for Gun\nEnter '3' For Exit")
    print("----------------------")
    user = int(input("Enter your Option : "))

    print()
    print(f"Your Choice : {user}")
    print(f"Computer's Choice : {comp}")
    print()
    score = check (user, comp)
    # print("s- ", score)
    if user == 3:
        print("Thankyou for Playing the Game !!")
        break
    elif score == 0:
        print("It's a tie")
    elif score == -1:
        print("You Lose !! Computer Win !!")
    else:
        print("Congraculations You Win !!!!!")


    
    
