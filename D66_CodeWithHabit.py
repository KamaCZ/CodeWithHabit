"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""


def word_checker(text):
    words = text.split()
    return words[0][0] == words[1][0]

print(word_checker("Chuck Noris"))

"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if 
one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""
def makes_twenty(a,b):
    if a == 20 or b == 20:
        return True
    elif a + b == 20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))


"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
"""

def mac_cap(macdonald):
    return macdonald[0:3].capitalize() +  macdonald[3:].capitalize()


print(mac_cap("macdonald"))












