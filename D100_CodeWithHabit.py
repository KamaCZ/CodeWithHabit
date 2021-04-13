# clearing out the screen
# in jupyter notebooks:
    # from IPython.display import clear_output
    # clear_output()


# in other IDEs:
    # print("\n" * 100)


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


test_board = ['#','X','O','X','O','X','O','X','O','X']

display_board(test_board)

"""
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
Think about using while loops to continually ask until you get a correct answer.
"""

def player_input():

    marker = " "

    while marker != "X" or marker != "O":
        marker = input("Do you want to be 'X' or 'O':").upper()

        if marker == "X":
            return("X", "O")

        if marker == "O":
            return("O", "X")


print(player_input())

"""
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) 
and assigns it to the board.
"""

def assign_position(board, marker, position):
    board[position] = marker

assign_position(test_board, "K", 8)
display_board(test_board)

"""
Step 4: Write a function that takes in a board and checks to see if someone has won.
"""

def check_win(board, marker):
    # checking rows
    return ((board[1] == board[2] == board[3] == marker) or 
    (board[4] == board[5] == board[6] == marker) or 
    (board[7] == board[8] == board[9] == marker) or
    # checking columns
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker) or 
    # checking diagonals
    (board[1] == board[2] == board[3] == marker) or
    (board[1] == board[2] == board[3] == marker))

print(check_win(test_board, "X"))

"""
Step 5: Write a function that uses the random module to randomly decide which player goes first. 
You may want to lookup random.randint() Return a string of which player went first.
"""

import random

def choose_player():
    if random.randint(0,1) == "0":
        return "X"
    else:
        return "O"

"""
Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
"""

def position_available(board, position):
    return board[position] == " "


"""
Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
"""

def check_full(board):
    return  " " not in board

    
"""
Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to 
check if its a free position. If it is, then return the position for later use.
"""

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not position_available(board,position):
        position = int(input("Enter position from 1 to 9:"))

    return position


"""
Step 9: Write a function that asks the player if they want to play 
again and returns a boolean True if they do want to play again.
"""
def play_again():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")


"""
Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
"""

