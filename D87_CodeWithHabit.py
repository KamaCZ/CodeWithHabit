"""
Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward 
as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to
 check out the .replace() method in a string to help out with dealing with spaces. 
 Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
"""

# using replace() and negative slicing
phrase = "nurses run"
phrase1 = phrase.replace(" ", "")
phrase2 = phrase1[::-1]
print(phrase1)
print(phrase2)

# solution:

def palindrome(phrase):
    phrase1 = phrase.replace(" ", "")
    phrase2 = phrase[::-1]
    return phrase1 == phrase2

print(palindrome("nurses run"))
print(phrase1)
print(phrase2)

# or:

def palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]   # Check through slicing

print(palindrome("nurses run"))


# trying one more time
def palindrome(s):
    s = s.replace(" ", "")
    s1 = s[::-1]
    print(s)
    print(s1)
    return s == s1
    #return s == s[::-1]

print(palindrome("nurses run"))
