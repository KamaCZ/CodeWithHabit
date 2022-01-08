# Guess Game

guessedWord = "New York"
numberGuesses = 0

while 0 <= numberGuesses < 3:

    guess = input("Enter a quessed word: ")
    if guess == guessedWord:
        print("You won the game! The guessed word was: " + guessedWord)
        break
    else:
        numberGuesses += 1

print("Sorry, you lost the game, you have no more guesses")

