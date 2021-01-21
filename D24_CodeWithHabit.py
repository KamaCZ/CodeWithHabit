# Tic Tac Toe Game

#----------Global Variables-------------


# Creating a playing board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game is still going
game_is_still_going = True

# who won? Or tie?
winner = None

# whose turn is it?
current_player = "X"


def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")


# play game of tic tac toe
def play_game():
    # display initial board
    display_board()
    # while the game is still going
    while game_is_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        # check if the game has ended
        check_if_game_over()
        # flip to the other player
        flip_player()


# the game has ended
if winner == "X" or winner == "O":
    print(winer + " won.")
elif winner == None:
    print("Tie")


# handle a single turn of an arbitrary player
def handle_turn(player):
    position = input("Choose a position from 1 to 9: ")
    position = int(position) - 1
    board[position] = "X"

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # check the rows
    row_winner = check_rows()
    # check the columns
    column_winner = check_columns()
    # check the diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # there is a win
    elif column_winner:
        # there is a win
    elif diagonal_winner:
        # there is a win
    else:
        # there was no win
    return


def check_rows():
    return


def check_columns():
    return


def check_diagonals():
    return


def check_if_tie():
    return


def flip_player():
    return





play_game()


# board
# display the board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player


# https://www.youtube.com/watch?v=4F2m91eKmts&list=PL-J2q3Ga50oMG2g_gCL66SVAK8VJzqt7t&index=6
# 5:28:00 stopped today

