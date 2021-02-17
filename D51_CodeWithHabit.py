# "in" operator

print(1 in [10,5,1])

print(1 not in [10,5,1])

# "min" and "max" checks the minimum or maximum of a list

print(min([10,5,1]))
print(max([10,5,1]))

# "random" python comes in with a built-in random library

import random
from random import shuffle
l = [1,10,5,30,40]
shuffle(l)
print(l)

# or we can access the functins of random this way (need to be started with "import random")
print(random.randint(0,100))


# list comprehensions can be used
# 1) simplified version of for loops
l = [1,5,10]
[print(num) for num in l]

# 2) to create lists, e.g. having a sentence and creating a list of all the letters inside the sentence
sentence = "Today is a beautiful day, isn't it babe?"
l2 = [letter for letter in sentence]
print(l2)

[print(letter) for letter in sentence]

# 3)to perform an operation on a list and creating another list affected by this operation (e.g. squering)

l_squared = [num**2 for num in l]
print(l_squared)

# 4) to square numbers in range and turn into list

l_squared1 = [num**2 for num in range(0,10)]
print(l_squared1)

# 5)if we want to create a new list from range, perform some action on that list and using "if" statement of top of that

lst = [x**2 for x in range(0,101) if x % 2 == 0]
print(lst)
print(len(lst))

# 6) convert celsius to fahrenheit
celsius = [-10,0,10,20,30]

fahrenheit = [(1.8 * temp)+ 32 for temp in celsius]
print(fahrenheit)

# 7) we can perform nested list comprehensions

lst = [x**2 for x in [x**2 for x in range(0,11)]]
print(lst)










