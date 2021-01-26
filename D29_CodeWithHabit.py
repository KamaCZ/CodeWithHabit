# TIC TAC TOE Game

# 1) printing the name of the game
# 2) def. game board
# 3) def. play game
#       displaying game boaard
#       handle turn function
#       check win
#       check tie
#       switching player
# 4) who is winner or if there is a tie


board = ["-","-","-","-","-","-","-","-","-"]

winner = None

game_still_going = True

current_player = "X"


def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

def play_game():
    global game_still_going
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_win()

        check_tie()

        switch_player()

    if winner == "X" or winner == "0":
        print(winner + " won.")
    else:
        print("This game ended with a tie!")


def handle_turn(player):
    return

def check_win():
    check_rows()
    check_columns()
    check_diagonals()

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

def check_tie():
    return

def switch_player():
    return






play_game()


        


