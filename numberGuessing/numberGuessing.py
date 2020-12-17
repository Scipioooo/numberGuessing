import random

print("I have a number between 0 and 100 in mind for you to find it.\r\nPropose a number!")
numberToGuess = random.randint(0, 100)
numberTried = -1

while numberToGuess != numberTried:
    try:
        numberTried = int(input())
    except ValueError:
        print("That's not a number ! Try again.")
        continue
    
    if numberToGuess < numberTried:
        print("Smaller !")
    elif numberToGuess > numberTried:
        print("Greater !")

print("Well done to you you found the number that was",numberToGuess,":)")