import random

l1 = list([x for x in range(1,101) if x % 2 == 1])
print(l1)
random.shuffle(l1)
print(l1)
print()

# sorting list items
l1.sort()
print(l1)

# reversing a list
l1.reverse()
print(l1)

# adding one item of the list to the end of the list
l1.append(101)
print(l1)

# taking out the last item of the list
l1.pop()
print(l1)

l1.append(1)

# counting the number of occurances of 1
print(l1.count(1))

# adding sequence of items to the end of the list
l1.extend([1,2,3])
print(l1)

# inserting an item into the list to the specific index
fruits = ["apple","lemon","pineapple"]
fruits.insert(1,"banana")
print(fruits)

# taking out duplicating values in a list
l2 = list(range(1,11)) * 10
print(l2)
random.shuffle(l2)
print(l2)
print()
t = set(l2)
print(t)

# removing the value in a list (the first occurance)
l3 = list(t)
print(l3)
l3.remove(3)
print(l3)

# using help method
print(help(l3.count))

