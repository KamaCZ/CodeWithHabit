"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up 
to and including a given number
Prime numbers are numbers that have only 2 distinct factors: itself and one. Meaning they are divisible only by one and itself

count_primes(100) --> 25
"""

def count_primes(num):

    # check for one and zero input
    if num <= 0:
        return 0
    #####################
    # number 2 or greater
    #####################

    # Store our prime numbers
    primes = [2]
    # Counter going up to the input num
    x = 3

    # x is going through every number up to the input num
    while x <= num:
        # check if prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    print(len(primes))

count_primes(100)

            


