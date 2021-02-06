# concatenating lists
names1 = ["Kamil", "Fred", "Thomas"]
names2 = ["Johan", "Andreas", "Thobias"]
names = names1 + names1
print(names)

# duplication method
names = names * 2
print(names)

# basic list methods:

# adding to the list (to the end of the list)
names1.append("HUGO")
print(names1)

# popping off the item from the list (by default the last item, but you can specifiy by stating the index)
names1.pop()
print(names1)
popped_item = names1.pop(0)
print(names1)
print(popped_item)

# sorting a list
names.sort()
print(names)

# nesting lists
num1 = [1,2,3]
num2 = [4,5,6]
num3 = [7,8,9]
num_keyboard = [num1, num2, num3]
print(num_keyboard[1][1])

# list comprehensions

for num_line in num_keyboard:
    print(num_line)
# the advantage of list comprehensions is that it enables to write a for loop in one line:
[print(num_line) for num_line in num_keyboard]

