# Tic Tac Toe Game

#----------Global Variables-------------


# Creating a playing board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game is still going
game_still_going = True

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
    while game_still_going:
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

    # Set up (access) global variable
    global winner
    # check the rows
    row_winner = check_rows()
    # check the columns
    column_winner = check_columns()
    # check the diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # there is a win
        winner = row_winner
    elif column_winner:
        # there is a win
        winner = column_winner
    elif diagonal_winner:
        # there is a win
        winner = diagonal_winner
    else:
        # there was no win
        winner = None
    return


def check_rows():
    # set up global variable
    global game_still_going
    # check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    # set up global variable
    global game_still_going
    # check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any row does have a match, flag that there is a win
    if column_1 or rcolumn_2 or column_3:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    # set up global variable
    global game_still_going
    # check if any of the diagonals have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # if any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner (X or O)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]X
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
# 5:38:30 stopped today
# start fixing en error at the beginning of D26

