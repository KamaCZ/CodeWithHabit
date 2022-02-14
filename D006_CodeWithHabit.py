# Guessing Game
# assignment:
# given a guessed word the player has 3 quesses to guess the word
# if he succeeds let him know that he won, if not let him know that he is out of guesses

guessed_word = "cat"
out_of_guesses = False
number_guesses = 3
your_guess = ""

while not out_of_guesses and your_guess != guessed_word:
    your_guess = input("Enter your guess: ")
    number_guesses = number_guesses - 1
    if number_guesses == 0:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, you lost the game, you are out of guesses.")
else:
    print("You won the game. Congratulation!")

