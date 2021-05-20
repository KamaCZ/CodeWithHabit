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




