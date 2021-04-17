
"""
Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
"""
def display_board(board):
    print("\n" * 100)
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

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
        return "Player 2"
    else:
        return "Player 1"


# While loop to keep running the game 
print("Welcome to TIC TAC TOE GAME")

while True:

    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHO FIRST, CHOOSE MARKERS - X,O)
    the_board = [" "] * 10

    player1_marker, player2_marker = player_input() 

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n: ")
    if play_game == "y":
        game_on = True
    else:
        game_one = False

    while game_on:

    ## PLAY GAME 

        if turn == "Player 1":
            # Show the board
            display_board(the_board)
            # Choose a position

            # Place the marker on the position

            # Check it they won

            # Check if there is a tie

            # No tie, no win, then next players turn





    ### PLAYER ONE TURN

        else:
            pass

    ### PLAYER TWO TURN

    if not replay():
        break
    # BREAK OUT ON THE WHILE LOOP 




