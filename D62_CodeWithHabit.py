lst = [1,2,3,4,5]
from random import shuffle
shuffle(lst)
print(lst)
"""
mylist = [" ","O"," "]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print(mylist)
shuffle_list(mylist)
print(mylist)
"""

original_list = [" ","O"," "]

def player_guess():
    guess = ""
    while guess not in ["0","1","2"]:
        guess = input("Pick a number, 0, 1, or 2: ")
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("correct guess!")
    else:
        print("Wrong, better luck next time")
        print(mylist)


mixedup_list = shuffle(original_list)
print(mixedup_list)

guess = player_guess()

check_guess(mixedup_list, guess)

# check the buggs
# check the bugs again babe