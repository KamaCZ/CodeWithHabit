# Methods

# methods perform specific actions on object and also can take arguments, just like a function
# methods are in the form:
    # object.method(arg1,agr2,etc...)
# we can think of methods as having an argument "self" referring to the object itself (OOP lesson!)

lst = [1,2,3,4,5]

lst.append(1)
print(lst)

print(lst.count(1)) # counting occurances of an object in a list

# print(help(lst.count)) # "help" function displays discription of the method

# other list methods:
# extend
lst2 = [10,20,30]
print(lst.extend(lst2))
print(lst)
# insert
print(lst.insert(0,0))
print(lst)
# pop
index2 = lst.pop(2)
print(index2)
print(lst)
print()
# remove
print(lst.remove(1))
print(lst)
# reverse 
print(lst.reverse())
print(lst)

# sort - sorts the object of the list in ascending order and returns "None"
print(lst.sort())
print(lst)





