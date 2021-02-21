"""
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
"""

import random
num = random.randint(1,100)

guesses = [0]

while True:

    guess = int(input("Enter a number from 1 to 100: "))
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue

    if guess == num:
        print(f"This is a correct number. Youd did it in {len(guesses)} tries")
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("WARMER")
        else:
            print("COLDER")

    else:
        if abs(num-guess) <= 10:
            print("WARM")
        else:
            print("COLD")





    


