# creating functions exercisesßß

"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""


def check_numbers(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)

print(check_numbers(2,4))
print(check_numbers(2,5))


"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

def word_checker(string):
    words = string.split()
    print(words)
    if words[0][0] == words[1][0]:
        return True
    else:
        return False


print(word_checker("Kamil Klemsa"))
print(word_checker("Freddy Mercury"))

# profi version:
def word_checker(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

print(word_checker("Kamil Klemsa"))
print(word_checker("Freddy Mercury"))




    






