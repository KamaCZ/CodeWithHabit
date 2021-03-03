# using of the "shuffle" function

lst = [1,2,3,4,5]
from random import shuffle

shuffle(lst)
print(lst)


# create a game using a programming logic, the player will guess the position of "O" which is located by shuffle function
# it can be locate on index 0,1, or 2. 

# 1) creating a list with 2 empty strings and the "O" string

mylist = ["","O",""]

# 2) creating a function that will shuffle the list

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# 3) creating a function returning the players guess

def player_guess():
    guess = ""
    while guess not in ["0","1","2"]:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)

# 4) function checking the players guess

def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("correct guess!")
    else:
        print("Wrong, better luck next time")
        print(mylist)

def play_game(mylist):

    mixedup_list = shuffle(mylist)

    guess = player_guess()

    check_guess(mixedup_list, guess)

play_game(mylist)


# check this bug: TypeError: 'NoneType' object is not subscriptable