# returning functions

def hello(name='Jose'):

    print("The hello function has been run.")
    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome


x = hello()


print(x())