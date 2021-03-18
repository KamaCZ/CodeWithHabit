
# Just for fun, not a real problem :)
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns. 
# For purposes of this exercise, it's ok if your dictionary stops at "E".

def print_big(letter):
    patterns = {1:"  *  ",2:" * * ",3:"*   *",4:"*****"}
    alphabet = {"A":[1,2,4,3,3]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big("a")

