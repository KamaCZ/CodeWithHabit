# Tic Tac Toe Game in 30 min :)

print("This is TIC TAC TOE Game. Enjoy!")

board = ["-","-","-","-","-","-","-","-","-",]

winner = None

current_player = "X"

game_still_going = True


def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + "|")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + "|")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + "|")


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_win()

        check_tie()

        flip_player()


    if winner == "X" or winner == "O":
        print(winner + " won.")
    else:
        print("It is a tie.")


def handle_turn(player):
    
    print(player + "'s turn.")
    position = input("Enter number from 1 to 9: ")

    position = int(position) - 1

    board[position] = player


def check_win():
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner  = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1:
        row_winner = board[0]
    elif row_2:
        row_winner = board[3]
    elif row_3:
        row_winner = board[6]
    else:
        row_winner = None
        

def check_columns():
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[5] != "-"
    column_3 = board[2] == board[7] == board[8] != "-"
    if column_1:
        column_winner = board[0]
    elif column_2:
        column_winner = board[1]
    elif column_3:
        column_winner = board[2]
    else:
        column_winner = None


def check_diagonals():
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
   
    if diagonal_1:
        diagonal_winner = board[0]
    elif diagonal_2:
        diagonal_winner = board[2]

    else:
        diagonal_winner = None

def flip_player():
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    



play_game()