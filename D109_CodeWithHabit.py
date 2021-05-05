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


display_board(board)
