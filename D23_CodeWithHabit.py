# Tic Tac Toe Game

# Creating a playing board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")


# defining play game function
def play_game():
    # display initial board
    display_board()

    while game_is_still_going:
    
        handle_turn(current_player)

        check_if_game_over()

        flip_player()


def handle_turn():
    position = input("Choose a position from 1 to 9: ")
    position = int(position) - 1
    board[position] = "X"

    display_board()


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
# 5:11:33 stopped today

