# filter function
# if you have function that returns True or False, then you can pass it to the filter function together with
# the iterator, you will get only the results that would turn True

def is_prime(num):
    """
    Checking if the number is prime
    """
    for i in range(2,num):
        if num % i == 0:
            return False
    else: # if never mod zero then prime
        return True

import random

l1 = list(range(2,101))
print(l1)
l2 = [random.choice(l1),random.choice(l1),random.choice(l1),random.choice(l1),random.choice(l1)]
print(l2)

print()
print(list(filter(is_prime,l2)))
