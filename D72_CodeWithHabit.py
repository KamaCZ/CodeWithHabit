"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) > 21 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return "BUST"

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


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
    




