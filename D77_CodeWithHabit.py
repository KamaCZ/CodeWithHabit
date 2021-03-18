# Lambda expressions
# map and filter functions


# MAP function
# is used when we want to apply a function to a list and iterate through it, it can be used instedad of "for loop"
# when we apply a "list" function on "map" functon we will get a list of results

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

map(square,my_nums)

for item in map(square, my_nums):
    print(item)


# for item in my_nums:
#     print(square(item))

print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]


names = ["Kamil","Lubos","Fido","Ben"]

print(list(map(splicer, names)))

# Filter function
# we can apply to a list when the result of the defined function is true or false, it will return items that are true

def check_even(num):
    return num%2 == 0

my_numbers = [1,2,3,4,5,6]

print(list(filter(check_even, my_numbers)))

for n in filter(check_even, my_numbers):
    print(n)

# LAMBDA expression
# anonymous functions
# we use them only once

def square(num): 
    return num**2

print(square(3))

fun = lambda num: num**2

print(fun(3))

print(list(map(lambda num: num**2, my_numbers)))

print(list(filter(lambda num: num%2 == 0, my_numbers)))





    





