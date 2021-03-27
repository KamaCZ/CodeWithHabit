# functions practising

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""

def unique(sample):
    return list(set(sample))

print(unique([1,1,1,1,2,2,3,3,3,3,4,5]))

# or:
def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

"""
Write a Python function to multiply all the numbers in a list.
Sample List : [1, 2, 3, -4]
Expected Output : -24
"""

def multiply(lst):
    total = 1
    for i in lst:
         total *= i
    return total

print(multiply([1, 2, 3, -4]))
