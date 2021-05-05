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

test_board = ["X"] * 10
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




