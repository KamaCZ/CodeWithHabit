"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up 
to and including a given number
Prime numbers are numbers that have only 2 distinct factors: itself and one. Meaning they are divisible only by one and itself

count_primes(100) --> 25
"""

def count_prime(num):

    if num < 2:
        return 0


    primes = [2]
    x = 3

    while x <= num:
        for n in range(3,x,2):
            if x%n == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    print(len(primes))

count_prime(100)



