# Nested Statements and Scope
# each variable has its scope which determines the visibility of the variable name for the rest of your code


# LEGB RULE

# L: Local - names assigned in any way within a functin such as def or lambda and they are not declaredd global in that function
# E: Enclosing function locals - names in the local scope of any and all enclosing functions (def or lambda), from inner and outer
# G: Global - names assigned at the top level of a module file or declared global within in a def within a file
# B: Built-in (Python) - names preassigned in the built-in names module: open, range etc.


# Local

lambda num: num**2


# Enclosing function locals

name = "This is a global string"

def greet():

    name = "SAMMY"

    def hello():
        print("Hello " + name)

    hello()

greet()

# Global

name = "This is a global string"

def greet():

    def hello():
        print("Hello " + name)

    hello()

greet()

# global
name = "This is a global string"

def greet():
    # enclosing
    name = "SAMMY"

    # local
    def hello():
        name = "I AM A LOCAL"
        print("Hello " + name)

    hello()

greet()


print(help(len))

