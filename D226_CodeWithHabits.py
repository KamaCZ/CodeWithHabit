# Lists

l1 = [1,2,"three"]

# Indexing
print(l1[1])

# Slicing
print(l1[1:])

# Concatenation
print(l1 + ["four",5])
l2 = l1 + ["four",5]
print(l2)

# multiplication
l3 = l2 * 5
print(l3)

# len function
print(len(l3))

# Adding item into a list
l3.append(6)
print(l3)

# popping an item
l_pop_last = l3.pop()
print(l_pop_last)
l_pop_first = l3.pop(0)
print(l_pop_first)
l_pop_middle = l3.pop(5)
print(l_pop_middle)

# Reversing a list
list1 = [1, 2, 3, 4, 1, 2, 6]
list1.reverse()
print(list1)

# Nested lists
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
l = [l1,l2,l3]
print(l)
print(l[2][2])

# list comprehensions
l = list(range(1,11))
print(l)
l2 = [x**2 for x in l]
print(l2)