"""
Assignment: Create a TIC TAC TOE GAME, two players playing, when the game is finished ask them if they want to play again.
"""

# creating a playing board, index zero will not be used

board = ["1"] * 10


# displaying the baord function

def display_board(board):

    # creating an empty space
    print("\n" * 100)

    # printing a board
    print(" " + " | " + " " + " | " + " ")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(" " + " | " + " " + " | " + " ")
    print("---------")
    print(" " + " | " + " " + " | " + " ")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(" " + " | " + " " + " | " + " ")
    print("---------")
    print(" " + " | " + " " + " | " + " ")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print(" " + " | " + " " + " | " + " ")


"""
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while 
loops to continually ask until you get a correct answer.
"""

# Asking one of the players if he wants to be X or O and assigning these markers to both players.

def player_input():

    """
    OUTPUT = (player1_marker, player2_marker) 
    """

    marker = ""

    while marker != "X" and marker != "O": # another option: while not (marker == "X" or marker == "O"):
        marker = input("Player1: Choose X or O: ").upper()
        
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")
    
# using tuple unpacking       
player1_marker, player2_marker = player_input()
print(player1_marker)




    