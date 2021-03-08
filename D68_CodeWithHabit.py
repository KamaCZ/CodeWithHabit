"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""

def master_yoda(text):
    return " ".join(text.split()[::-1])

print(master_yoda("It is a beautiful day babe."))


"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
"""

def almost_there(n):
    return 89 < n < 111 or 189 < n < 211
        

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# or using "abs":

def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))




