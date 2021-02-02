# Global and local scope
# Global and local vairables¨


# Global scope for a global variable is created when the program starts, and destroyed when the program ends
# Local scope for a local variable is creadted whend the fucntion is called and destroyed when the function returns


# Rules:
# 1) Code in the global scope cannot use any local variables
# example:
def spam():
    eggs = 99

spam()
print(spam)

# 2) Code in the local scope can access global variable
# example:
def spam():
    print(eggs)

eggs = 42
spam()  # remark: but if there is an assignment statement in the function than the variable is considered a local variable
# example:
def spam():
    eggs = "Hello"
    print("eggs")

eggs = 100
spam()
print(eggs)
# example of accessing a global variable:
print("Example of accessing a global variable")
def spam():
    global eggs
    eggs = "Hello"
    print(eggs)

eggs = 42
spam()
print(eggs)
print("End of the global variable")



# 3) Code in one function's local scope cannto use variables in any other local scope (local variables from different function are completely separate)
# example:
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

