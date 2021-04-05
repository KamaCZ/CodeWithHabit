"""
Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
"""

print("This is a tic tac toe game")

board = [" "," "," "," "," "," "," "," "," "]

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


display_board()


def play_game():
    pass




play_game()