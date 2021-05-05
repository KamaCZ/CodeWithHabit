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
# player1_marker, player2_marker = player_input()


"""
A Function that takes in the board list object, a marker ('X' or 'O'),
and a desired position (number 1-9) and assigns it to the board.
"""

def place_marker(board,marker,position):
    board[position] = marker
    

"""
Running a text - providing arguments to place_marker function and displaying board
"""

test_board = [" "] * 10


#place_marker(test_board,"O",4)




"""
Funciton that takes in the board and checks if someone has won
"""
# check the solution in the course, I coded it a little bit different way
def check_win(board):
    return ((board[1] == board[2] == board[3] != " ") or # winning a bottom row
    (board[4] == board[5] == board[6] != " ") or # winning a middle row
    (board[7] == board[8] == board[9] != " ") or # winning an upper row
    (board[1] == board[4] == board[7] != " ") or # winning left column
    (board[2] == board[5] == board[8] != " ") or # winning middle column
    (board[3] == board[6] == board[9] != " ") or # winning right column
    (board[1] == board[5] == board[9] != " ") or # winning diagonal 1
    (board[3] == board[5] == board[6] != " ")) # winning diagonal 2



"""
Function that uses the random module to randomly decide which player goes first. You may want 
to lookup random.randint() Return a string of which player went first.
"""

import random

def who_first():

    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

"""
Function that returns a boolean indicating whether a space on the board is freely available.
"""
# I didnt use this function later on, instead I replaced it with a simple code within the function called player_choice
def available(board,position):

    return board[position] == " "

"""
Function that checks if the board is full and returns a boolean value. True if full, False otherwise.
"""

def full_board(board):

    for i in board:
        if i == " ":
            return False
    return True



"""
Function that asks for a player's next position (as a number 1-9) 
and then uses the function from step 6 to check if its a free position. If it is, 
then return the position for later use.

"""

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not board[position] == " ":
        position = int(input('Choose your next position: (1-9) '))
        
    return position



"""
Step 9: Write a function that asks the player if they want to play again
and returns a boolean True if they do want to play again.
"""

def replay():

    return input("Do you want to play again? Enter Yes or NO").lower().startswith("y")

    
##################################
######### Setting up the Game ###
#################################

# While loop to keep running the game
print()
print("Welcome to TIC TAC TOE \n \n")

while True:

    # Play the game

    ## Setting up the board
    the_board = [" "] * 10
    ## Player1 will choose if he want to be X or O, Player2 will be automatically assigned the second marker
    player1_marker, player2_marker = player_input()
    # program will automatically decide who will play first, either Player1 or Player2, the information is given to players
    turn = who_first()
    print(turn + " will go first")
    # asking the players if they want to play the game now
    play_game = input("Do you want to play now? y or n? ")
    if play_game == "y":
        game_on = True
    else:
        game_on = False

    ## Game play

    while game_on == True:

         ### Player1 turn
        if turn == "Player1":
            # show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(board)

            # place a marker to the position
            place_marker(the_board,player1_marker,position)

            # check for win
            if check_win(board):
                display_board(board)
                print("Player1 has won.")
                game_on = False
            else:
                # check for tie
                if full_board(board):
                    display_board(board)
                    print("There is a tie.")
                    
                # no win, no tie, next player's choice
                else:
                    pass


        
        else:  
         ### Player two turn
            pass










    # Checking if the players want to play again
    if not replay():
        break






