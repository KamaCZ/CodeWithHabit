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

