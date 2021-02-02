from typing import NoReturn


print()
print("this is Tic Tac Toe Game. Enjoy!")
print()


board = ["-","-","-","-","-","-","-","-","-",]

winner = None

game_still_going = True

current_player = "X"

def display_board():
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")


def play_game():
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_win()

        check_tie()

        flip_player()


    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")

def handle_turn(player):
    print(player + "'s turn.")
    position = input("Enter number from 1 to 9: ")
    position = int(position) - 1
    board[position] = player
    display_board()
    return

def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()

# I did a bug = showing me a tie after entering a position
"""
check if a elif
check global variables
check the whole logic
make a video commenting this game
check handle_turn - errors while entering wrong data
"""