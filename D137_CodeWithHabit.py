# decorators part 1

s = "Global Variable"

#print(globals())
#print(locals())

print(globals().keys())

def func():
    print(locals())


func()

def hello(name="Kama"):
    print("Hello " + name)

hello()

greet = hello

greet()

del hello

greet()

# decorators part 2

print(globals()["__name__"])
print(globals())
print()
print(globals().keys())


def hello(name="Kama"):
    print("The hello() function has been executed.")

    def greet():
        return "\t This is inside the greet() function."

    def welcome():
        return "\t This is inside the welcome() function."

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function.")

hello()

# decorators part 3

def hello(name='Jose'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome

print(hello())
print()
print(hello()())

# Now lets see how we can pass functions as arguments into other functions:
print()
print()
def hello():
    return "Hi Jose"

def other(func):
    print("other code would go here")
    print(func())

other(hello)

# decorators part 4
print()
print()


def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func


def func_needs_decorator():
    print("This function is in need of a Decorator")
    print()


func_needs_decorator()

func_needs_decorator = new_decorator(func_needs_decorator)


# check it tomorrow

func_needs_decorator()



