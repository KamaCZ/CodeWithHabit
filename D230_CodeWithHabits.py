# tuples
# tuples are compared to list immutable, meaning that the items cant be changed
# we use them for things that are not supposed to be changed, e.g. months, days of the week etc.

# tuple example
t = (1,5,6,2,"three")
print(t)
print(t[2])
print(t[-1])

#converting list into a tuple:
t = tuple(list(range(10)))
print(t)
print(len(t))

# tuple methods
# index() - entering a value and returning index
print(t.index(6))

# count() - entering a value and returning number of appearences in the tuple
print(t.count(3))



