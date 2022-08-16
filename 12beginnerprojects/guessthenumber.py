#Guess the number game
#Goodluck

import random

def guess(x):
    random_number = random.randint(1,x)
    return random_number


print("welcome to the guessing number game")
max_number = int(input("Enter max number: "))

playing_number =guess(max_number)
playing = True
counter = 0

while playing:
    number = int(input(f"Guess the number between 1 and {max_number}: "))
    if(number == playing_number):
        print("YOU ARE CORRECT")
        print(f"It took you {counter} times to guess correctly")
        playing = False
    elif (number > playing_number):
        print("Go lower")
        counter = counter + 1
    elif (number < playing_number):
        print("Go higher")
        counter = counter + 1

        





