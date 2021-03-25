# *args and **kwargs

def funct(*args):
    return sum(args) * 0.05

print(funct(5,10,15,20))


# **kwargs = key word arguments
# returns back a dictionary

def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}.".format(kwargs["fruit"]))

myfunc(fruit = "apple", weggie = "brocolli", drink = "cola", sidedish = "potato", maindish = "chicken", dessert = "pavlova")

# combination of args and kwargs

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs["food"]))

myfunc(10,20,30, fruit="orange", food="eggs", animal="dog")