# range function: "range()"
# creates an object that returns the successive items of the desired sequence
# you can pass the object items to a list function to create a list

iter_object = range(10)
print(list(iter_object))
iter_object1 = range(0,10)
print(list(iter_object))


# you can iterate through this items
for num in iter_object:
    print(num)


# pass statement - does nothing, it can be used when a statement is required syntactically, but the program requires no action, e.g.:
#while True:
 #   pass 

class MyEmptyClass:
    pass

def myFunction():
    pass # remember to implement this

# return statement
# is used inside a defining function
# return the value of the function, without execution of the statement coming after the return statement e.g.

def myNewFunction(player):
    return