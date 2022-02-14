# functions in python

# what is function: 
# function is a bunch of statements (code) that we put together in the expectation that it will be run more times 

# how we create functions in Python:
# we start with "def" then " " then the name of the function, then we can put some arguments into the brackets
# these arguments are inputs into the function and can be worked with inside the function
# then you need to indent
# then within the docstrings you will write simple description of the function
# then you follow up with the body of the function

# assignment: create a function that takes a number as an arguments and returns True if it is Prime number
# return False if not
# definition of a prime number: number that is greater than 1 and is divisible only by itself and 1, cant be a negative number

# great youtube video on prime numbers solution: https://www.youtube.com/watch?v=SpTAxH_Geow

# version 1# function is a bunch of statements (code) that we put together in the expectation that it will be run more times 
def is_prime(num):
    """
    Checking if the number is prime
    """
    for i in range(2,num):
        if num % i == 0:
            return False
    else: # if never mod zero then prime
        return True

print(is_prime(51))

# Version 2
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

is_prime(13)
