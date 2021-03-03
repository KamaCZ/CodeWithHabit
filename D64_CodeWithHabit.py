# function exercises

"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""

def number_checker(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    if num1 % 2 != 0 or num2 % 2 != 0:
        if num1 > num2:
            return num1
        else:
            return num2

result1 = number_checker(2,4)
result = number_checker(2,5)
print(result1)
print(result)


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)