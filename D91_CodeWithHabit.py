"""
Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
"""

print("This is a tic tac toe game")

board = [" "," "," "," "," "," "," "," "," "]

winner = " "

game_still_going = True

current_player = "X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():

    display_board()
    
    while game_still_going:

        make_turn(current_player)    
    

def make_turn(current_player):

    print("This is " + current_player +"'s turn:")
    position = int(input("Choose your position from 1 to 9: "))
    position = position - 1
    board[position] = current_player
    display_board()
        


play_game()