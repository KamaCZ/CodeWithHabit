# SCOPE of the variable
# when you declare a variable inside a function definition, they are not related in any way
# to other variables with the same name outside the function

x = 50

def func(x):
    print("x is", x)
    x = 2
    print("changed local x to", x)


func(x)
print("x is still", x)

# The Global statement
# if you want to assign a global variable in the local scope (inside defining a function), you need to use the "global" statement

# To check what are your global and local variables:
#print(globals())
print(locals())
