# map function
# map function allows you to map a function to an iterable object

def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')

    
import random

l1 = list(range(2,101))
print(l1)
l2 = [random.choice(l1),random.choice(l1),random.choice(l1),random.choice(l1),random.choice(l1)]
print(l2)

list(map(is_prime, l2))