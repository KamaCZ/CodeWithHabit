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

# First, pick a random integer from 1 to 100 using the random module and assign it to a variable¶
import random
num = random.randint(1,100)
print()
print("Welcome to the Guess Game")
print()
print("I am thinking of a number between 1 and 100.")
print("If your guess is more than 10 away from my number, I will tell you are 'COLD'.")
print("If your guess is within 10 of my number, I will tell you are 'WARM'.")
print("If your guess is further than your most recent guess, I will say you are getting colder.")
print("If your guess is closer than your most recent guess, I will say you are getting warmer.")
print("If you guess the number correctly, than I will say you that you did it and how many guesses you took.")
print()

# Create a list to store guesses¶

guesses = [0]

# Write a while loop that asks for a valid guess. Test it a few times to make sure it works.

while True:
    guess = int(input("Enter the number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Please try again: ")
        continue

    if guess == num:
        print("It took {} guesses to guess the word.".format(len(guesses)))
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



    




    



    







