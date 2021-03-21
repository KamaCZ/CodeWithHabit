# Nested Statements and Scope
# each variable has its scope which determines the visibility of the variable name for the rest of your code

x = 25

def printer():
    x = 50
    return x

print(x)

print(printer())


# Local

f = lambda x: x**2
print(f(5))
