# scopes in PYTHON
# when you create a variable in Python, the variable is stored in a scope
# the scope determines the visibility of that variable name to other parts of the code
# LEGB rules in terms of scope:
# L: Local:  variables (names) assigned in any way withing a function (def or lambda) and not declared global
# E: Enclosing function local: variables in the local scope of any enclosing function (function in a function)
# G: Global: variables assigned at the top level of a module file, or declared global withing a def or lambda
# B: Built-in: names preassigned in the built-in names module, never reaasign (overwrite built-in names)

# nested statements = function inside a function, the examples below


# assigning a global variable
x = 25

# assigning local variable
def printer():
    x = 50
    return x

print(printer())
print(x)

# assigning a global variable name
name = "This is a global name"

def greet():
    # assigning a enclosing variable name
    name = "John"
    print(f"enclosing local variable is {name}")

    def hello():
        # assigning a local variable name
        name = "Fred"
        print(f"Hello {name}")
    hello()

greet()
print(name)

# 2 ways of declaring global variable inside a local scope

# 1) using a global key word
x = 25

def printer():
    global x
    x = 50
    print(x)

printer()
print(x)

# asigning (cleaner way when you deal with more complex code)
x = 25

def printer():
    x = 50
    return x

print(printer())
x = printer()
print(x)





