# TIC TAC TOE GAME - coding on time
# time limit: 30 min
print()
print("This is TIC TAC TOE Game. Enjoy!")
print()

board = ["-","-","-","-","-","-","-","-","-",]

game_still_going = True

winner = None

current_player = "X"


def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")

def play_game():
    global game_still_going

    display_board()

    handle_turn()

    check_win()

    check_tie()

    flip_player()
     

def handle_turn():
    return

def check_win():
    return

def check_tie():
    return

def flip_player():
    return

if winner == "X" or winner == "O":
    print(winner + "won.")
else:
    print("It is a tie. Nobody won")



play_game()






# 1) Defining board
# 2) Defining play game function
        # display the board
        # handle turn
        # check for win
            # check rows
            # check columnts
            # check diagonals
        # chek for tie
        # flip player
# 3) Letting know who won or if it was a tie.
