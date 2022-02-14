# create a function that will for each letter/sign in a given string will print the following:
# "At idnex 0 the letter is "letter in the string" etc until the end of the string

def index_letter(string):
    index_count = 0
    for letter in string:
        print(f"At index {index_count} the letter is {letter}")
        index_count += 1

index_letter("Today is my Birthday.")

# enumerate function
# counts in background the number of iterations, is good to use with for loops
# in the following we will get the same result as the function above:

def index_letter(string):
    for i,letter in enumerate(string):
        print(f"At index {i} the letter is {letter}")

index_letter("Today is my Birthday.")