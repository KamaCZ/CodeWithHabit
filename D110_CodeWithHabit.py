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

# Asking one of the players if he want to be X or O and assigning these markers to both players.

def assign_marker():

    player = " "

    while player != "X" or player != "O":
        player = input("Do you want to be a player 'X' or 'O'? Enter 'X' or 'O': ").upper()
        print(player)
    if player == "X":
        player_X, player_O = ("X","O")
    else:
        player_O, player_X = ("O","X")
    print(player_X, player_O)
        
assign_marker()


# check this bug tomorrow wou

    