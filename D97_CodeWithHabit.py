# clearing out the screen
# in jupyter notebooks:
    # from IPython.display import clear_output
    # clear_output()


# in other IDEs:
    # print("\n" * 100)


def display_board(board):
    print("\n" * 100)
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


test_board = ['#','X','O','X','O','X','O','X','O','X']

display_board(test_board)

"""
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
Think about using while loops to continually ask until you get a correct answer.
"""

def player_input():

    marker = " "

    while marker != "X" or marker != "O":
        marker = input("Do you want to be 'X' or 'O':").upper()

        if marker == "X":
            return("X", "O")

        if marker == "O":
            return("O", "X")


print(player_input())

"""
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) 
and assigns it to the board.
"""



