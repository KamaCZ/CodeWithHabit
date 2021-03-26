# Functions training

"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

If you feel ambitious, explore the Collections module to solve this problem!
"""

def count_lower_upper(text):
    lowers = 0
    uppers = 0
    for letter in text:
        if letter.isupper():
            uppers += 1
        elif letter.islower():
            lowers += 1
        else:
            pass
    print("The length of the string is " + str(len(text)) + ".")
    print("Of which lower case letters are : {}".format(lowers))
    print("Of which upper case latters are: {}".format(uppers))

count_lower_upper("My name is Kamil, I am a cute guy whol lives in Czech Republic, Norway, and Indonesia.")

# another solution:

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

s = "My name is Kamil, I am a cute guy whol lives in Czech Republic, Norway, and Indonesia."
up_low(s)






