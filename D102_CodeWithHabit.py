
"""
Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
"""

def player_input():

    marker = " "

    while marker != "X" or marker != "O":
        marker = input("Do you want to be 'X' or 'O':").upper()

        if marker == "X":
            return("X", "O")

        if marker == "O":
            return("O", "X")

def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")

import random

def choose_first():
    if random.randint(0,1) == "0":
        return "X"
    else:
        return "O"


# While loop to keep running the game 
print("Welcome to TIC TAC TOE GAME")

while True:

    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHO FIRST, CHOOSE MARKERS - X,O)
    board = [" "] * 10

    player1_marker, player2_marker = player_input() 

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? ")

    ## PLAY GAME 

    ### PLAYER ONE TURN

    ### PLAYER TWO TURN

    if not replay():
        break
    # BREAK OUT ON THE WHILE LOOP 




