# Lambda expressions
# allow us to create anonymous functions, we can create ad-hoc functions instead of creating def...
# compared to def, lambda expresssion is a single expression not a block of code
# lambda is designed to code single one-time functions

# function to square a nunber
def square(num):
    result = num**2
    return result
print(square(2))

# simplified version of a functin to square a number
def square(num):
    return num**2
print(square(2))

# you can write the function to square the number this way as well:
def square(num): return num**2
print(square(2))

# checking the object type
print(type(lambda num: num**2))

# lambda expression substituting the square function
square = lambda num: num**2
print(square(2))

# shuffling the list of numbers
import random
my_list = list(range(1,11))
random.shuffle(my_list)
print(my_list)

# using a map function to get the squared numbers 
def square(num):
    return num**2

print(list(map(square, my_list)))

# using lambda expression together with map function to get the squared numbers
lambda num: num**2

result = list(map(lambda num: num**2, my_list))
print(result)

# using a filter function to get even numbers
def even(num):
    return num % 2 == 0

print(list(filter(even, my_list)))

# using lambda expression together with filter function to get the even numbers
lambda num: num % 2 == 0

result = list(filter(lambda num: num % 2 ==0, my_list))
print(result)

# ** Lambda expression for grabbing the first character of a string: **
def grab_first(string):
    return string[0]

print(grab_first("Kamil"))

grab_first = lambda f: f[0]

print(grab_first("Kamil"))

list_names = ["Kamil", "Fred", "Ziky", "Jonathan)"]

print(list(map(lambda f: f[0], list_names)))

# we can use lambda expressions even for more arguments
result = lambda x,y: x+y
print(result(2,3))

# not every function can be translated to lambda expression
# some 3rd party modules like pandas works really well with lambda expressions




