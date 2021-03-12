"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of 
numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""

def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1, 3, 5])) 
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


"""
PY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
 """

def spy_game(lst):

    code = [0,0,7,"x"]

    for num in lst:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1
    # return code == []
# check why return code == [] doesnt work


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))





        
