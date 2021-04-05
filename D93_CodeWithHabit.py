"""
Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
"""

print("This is a tic tac toe game")

board = [" "," "," "," "," "," "," "," "," "]

winner = None

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

        check_win()

        check_tie()

        switch_player()
        

    if winner == "X" or winner == "O":
            print("The winner is :" + winner)
    else:
        print("It is a tie!")


def make_turn(current_player):

    print("This is " + current_player +"'s turn:")
    position = int(input("Choose your position from 1 to 9: "))
    while position not in [0,1,2,3,4,5,6,7,8,9]:
        print("You entered a wrong position. Try again!")
        break
    else:
        position = position - 1
        board[position] = current_player
    display_board()
        
def check_win():
    check_rows()
    check_columns()
    check_cross()


def check_rows():
    global winner
    global game_still_going

    if board[0] == board[1] == board[2] != " ":
        winner = board[0]
    elif board[3] == board[4] == board[5] != " ":
        winner = board[3]
    elif board[6] == board[7] == board[8] != " ":
        winner = board[6]
    game_still_going = False
    

def check_columns():
    pass

def check_cross():
    pass

def check_tie():
    pass

def switch_player():
    pass

play_game()


# check the bugs