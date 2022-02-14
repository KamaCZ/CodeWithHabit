# *args and **kwargs
# these strange terms show up as parameters in function definition

def my_func(a,b):
    return sum((a,b)) * 0.05
print(my_func(40,60))

# This function returns 5% of the sum of a and b. In this example, 
# a and b are positional arguments; that is, 40 is assigned to a because it is the first argument, 
# and 60 to b. Notice also that to work with multiple positional arguments 
# in the sum() function we had to pass them in as a tuple.

# What if we want to work with more than two numbers?
# One way would be to assign a lot of parameters, and give each one a default value.

def my_func(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e)) * 0.05

print(my_func(60,40,100))

# args
# when a functions parameter starts with * it allows for an arbitrary number of arguments, 
# and the function takes them as a tuple of values

def my_func(*args):
    return sum(args) * 0.05

print(my_func(50,50,100,60,40))

# note that * can be followed by any string

def my_func(*spam):
    return sum(spam) * 0.05

print(my_func(50,50,100,60,40))

# **kwargs
# Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. 
# Instead of creating a tuple of values, 
# **kwargs builds a dictionary of key/value pairs. For example:

# not using kwargs:
def my_func(dict):
    if "key1" in dict:
        print(f"The key1 needed for a transaction is {dict['key1']}")
    else:
        print("The key1 is not available")

dict1 = {"key1": 25, "key2": 65, "key3": 101}
my_func(dict1)

# using kwargs:
def my_func(**kwargs):
    if "key1" in kwargs:
        print(f"The key1 value needed for a transaction is {kwargs['key1']}")  
    else:
        print("The key1 value is not defined.")      

my_func(key1= 25, key2 = 65)

# another example:
def my_func(**kwargs):
    if "fruit" in kwargs:
        print(f"My favourite fruit is {kwargs['fruit']}")
    else:
        print("I dont have a favourite fruit")

my_func(fruit="apple",name="Kamil",number=32)

# args and kwargs in the same function

t = ("Kamil","Luboš")
print(" and ".join(t))

l = ["Kamil","Luboš", "John"]
print(" and ".join(l))

def my_func(*args,**kwargs):
    if "fruit" and "drink" in kwargs:
        print(f"I ususally eat {' and '.join(args)} with {kwargs['fruit']} {kwargs['drink']}.")
    else:
        print("I dont have any preferences.")
   
my_func("eggs","bacon",fruit= "oragne",drink= "juice")




























