"""
Hard:
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons
"""
import string

def pangrams(str1, alphabet=string.ascii_lowercase):
    # create a set of alphabet
    alphaset = set(alphabet)

    # remove spaces from string
    str1 = str1.replace(" ", "")

    # lowercase all the letters
    str1 = str1.lower()

    # create a set to get all the unique letters
    str1 = set(str1)

    # now check that the alpahbet set is the same like the string set
    return str1 == alphaset


print(pangrams("The quick brown fox jumps over the lazy dog"))


