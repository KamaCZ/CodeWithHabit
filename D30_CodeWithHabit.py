# Tic Tac Toe Game
print()
print("This is Tic Tac Toe Game. Enjoy")
print()

board = ["-","-","-","-","-","-","-","-","-",]

game_still_going = True

current_player = "X"

winner = None

def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")

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
        print("The game is a tie!")

def handle_turn(player):
    print(player + "'s turn")
    position = input("Enter a number from 1 to 9: ")

    if position not in ["1","2","3","4","5","6","7","8","9"]:
        print("Invalid input. You must write number 1 to 9!")
    else:
        position = int(position) - 1
        board[position] = player
    return

def check_win():
    return

def check_tie():
    return

def flip_player():
    return


play_game()
