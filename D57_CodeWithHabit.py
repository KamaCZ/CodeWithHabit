# Functions

# we use functions when we expect we would need to use bunch of the same code repeatedly
# each function we start to create with "def" followed by the functins name with paranthesis. Inside paranthesis we can state arguments
# (inputs of the function). Parenthesis are followed with collon. Than on the next line we should write a description of the function (docstrings). 
# Text in the docstrings starts with """ and ends with """. Than the text of the function follows.

# function calling you by name

def say_hello(name):
    print(f"Hi {name}. What's upt?")

# calling the function
say_hello("Kamil")

# if we want to store the results of the function we must use "return" statements, than we can assign the result to a variable

def add_num(num1, num2):
    return num1 + num2

result = add_num(100, 99)
print(result)
