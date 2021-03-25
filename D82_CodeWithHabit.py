# *args and **kwargs
# two functional parameters
# *args = star args = stands for arguments
# **kwargs = double star kwargs = stands for k-word arguments


def myfunc(a,b):
    # returns 5% of the sum a and b
    return sum((a,b))* 0.05

print(myfunc(40,60))

# in case we want to pass more arguments:

def myfunc(a,b,c=0,d=0,e=0):
    # returns 5% of the sum a and b
    return sum((a,b,c,d,e))* 0.05

print(myfunc(40,60,100))

def myfunc(*args): # passing * args argument allows me to deal with it like a tuple of arguments
    return sum(args) * 0.05

print(myfunc(40,60,200))

# args can be any word, e.g. spam
# args is passed a tuple
def myfunc(*spam): # note: we can use any word after the *
    return sum(spam)