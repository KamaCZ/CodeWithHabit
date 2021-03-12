"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""

def paper_doll(text):
    result= ""
    for i in text:
        result += i * 3
    return result

print(paper_doll("Today is a beautifull day."))

"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""
"""
def blackjack(num1, num2, num3):
    if (num1 + num2 + num3) <= 21:
        return num1 + num2 + num3
    elif ((num1 + num2 + num3) > 21) and (num1 or num2 or num3 == 11):
        return num1 + num2 + num3 -10
    elif ((num1 + num2 + num3 - 10) > 21):
        return "BUST"

------- WROOOOONG

print(blackjack(1,10,10))
"""


def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'




