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
print()

def hello():
    return "Hi Kama"

def other(func):
    print("Hello")
    print(func)

other(hello)

# versus:

def hello():
    return "Hi Kama"

def other(func):
    print("Hello")
    print(func())

other(hello)


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator.")

# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

    