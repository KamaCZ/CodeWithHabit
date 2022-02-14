# random module
# built-in module
# shuffle lists, generate random numbers

import random

# shuffle function to shuffle the original list
l1 = list(range(1,101))
print(l1)
random.shuffle(l1)
print(l1)

# generating a shuffled item from a range (including the threshold values)
print(random.randint(0,100))

# generating a random number between 0 and 1
print(random.random())

# choosing a random item out of your list
print(random.choice(l1))