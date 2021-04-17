
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
        return "Player2"
    else:
        return "Player1"

def space_check(board,position):
    return board[position] == " "

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(the_board,position):
        position = int(input("Enter position from 1 to 9:"))

    return position


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    # checking rows
    return ((board[1] == board[2] == board[3] == marker) or 
    (board[4] == board[5] == board[6] == marker) or 
    (board[7] == board[8] == board[9] == marker) or
    # checking columns
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker) or 
    # checking diagonals
    (board[1] == board[5] == board[7] == marker) or
    (board[3] == board[5] == board[9] == marker))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

"""
def full_board_check(board):
    return  " " not in board
"""

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
        game_on = False

    while game_on:

    ## PLAY GAME 
       
        if turn == "Player1":
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player1_marker,position)
            # Check it they won

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won.")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game")
                    break
                else:
                    turn = "Player2"
           
        else:
            if turn == "Player2":
                # Show the board
                display_board(the_board)
                # Choose a position
                position = player_choice(the_board)
                # Place the marker on the position
                place_marker(the_board,player2_marker,position)
                # Check it they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("Player 2 has won.")
                    game_on = False

                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("Tie Game")
                        break
                    else:
                        turn = "Player1"


    if not replay():
        break
    # BREAK OUT ON THE WHILE LOOP 




