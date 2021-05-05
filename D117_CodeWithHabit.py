"""
Assignment: Create a TIC TAC TOE GAME, two players playing, when the game is finished ask them if they want to play again.
"""

# creating a playing board, index zero will not be used

board = ["1"] * 10


# displaying the baord function

def display_board(board):

    # creating an empty space
    print("\n" * 100)

    # printing a board
    print(" " + " | " + " " + " | " + " ")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(" " + " | " + " " + " | " + " ")
    print("---------")
    print(" " + " | " + " " + " | " + " ")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(" " + " | " + " " + " | " + " ")
    print("---------")
    print(" " + " | " + " " + " | " + " ")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print(" " + " | " + " " + " | " + " ")


"""
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while 
loops to continually ask until you get a correct answer.
"""

# Asking one of the players if he wants to be X or O and assigning these markers to both players.

def player_input():

    """
    OUTPUT = (player1_marker, player2_marker) 
    """

    marker = ""

    while marker != "X" and marker != "O": # another option: while not (marker == "X" or marker == "O"):
        marker = input("Player1: Choose X or O: ").upper()
        
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")
    
# using tuple unpacking       
player1_marker, player2_marker = player_input()


"""
A Function that takes in the board list object, a marker ('X' or 'O'),
and a desired position (number 1-9) and assigns it to the board.
"""

def place_marker(board,marker,position):
    board[position] = marker
    

"""
Running a text - providing arguments to place_marker function and displaying board
"""

test_board = [" "] * 10
display_board(test_board)

place_marker(test_board,"O",4)

display_board(test_board)


"""
Funciton that takes in the board and checks if someone has won
"""
# check the solution in the course, I coded it a little bit different way
def check_win(board):
    return ((board[1] == board[2] == board[3] != " ") or # winning a bottom row
    (board[4] == board[5] == board[6] != " ") or # winning a middle row
    (board[7] == board[8] == board[9] != " ") or # winning an upper row
    (board[1] == board[4] == board[7] != " ") or # winning left column
    (board[2] == board[5] == board[8] != " ") or # winning middle column
    (board[3] == board[6] == board[9] != " ") or # winning right column
    (board[1] == board[5] == board[9] != " ") or # winning diagonal 1
    (board[3] == board[5] == board[6] != " ")) # winning diagonal 2

print(check_win(test_board))

"""
Function that uses the random module to randomly decide which player goes first. You may want 
to lookup random.randint() Return a string of which player went first.
"""

import random

def who_first():

    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

"""
Function that returns a boolean indicating whether a space on the board is freely available.
"""
# I didnt use this function later on, instead I replaced it with a simple code within the function called player_choice
def available(board,position):

    return board[position] == " "

"""
Function that checks if the board is full and returns a boolean value. True if full, False otherwise.
"""

def full_board(board):

    for i in board:
        if i == " ":
            return False
    return True

print(full_board(test_board))

"""
Function that asks for a player's next position (as a number 1-9) 
and then uses the function from step 6 to check if its a free position. If it is, 
then return the position for later use.

"""

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not board[position] == " ":
        position = int(input('Choose your next position: (1-9) '))
        
    return position

print(player_choice(test_board))


"""
Step 9: Write a function that asks the player if they want to play again
and returns a boolean True if they do want to play again.
"""

def play_again():

    return input("Do you want to play again? Enter Yes or NO").lower().startswith("y")

    






