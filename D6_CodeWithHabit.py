# Guessing Game

guessedWord = "Christmas"
guess = ""
guesslimit = 3
numberGuesses = 0
outOfGuesses = False


while guess != guessedWord and not outOfGuesses:
    if numberGuesses < guesslimit:
        guess = input("Enter your guessed word: ")
        numberGuesses += 1
    else:
        outOfGuesses = True

if outOfGuesses == True:
    print("You already guessed 3 times and did not guessed the number!")
else:
    print("You guessed the word. Congratulation")
