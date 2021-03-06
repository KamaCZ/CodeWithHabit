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
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    cross_winner = check_cross()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif cross_winner:
        winner = cross_winner
    else:
        winner = None


def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != " "
    row2 = board[3] == board[4] == board[5] != " "
    row3 = board[6] == board[7] == board[8] != " "
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    

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