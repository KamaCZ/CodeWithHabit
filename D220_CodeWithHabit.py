# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based
#  on the values of an existing list.

# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "p" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["banana","apple","appricote","pear"]
p_fruits = []

for fruit in fruits:
    if "p" in fruit:
        p_fruits.append(fruit)

print(p_fruits)

# using list comprehensions

p_fruits = [fruit for fruit in fruits if "p" in fruit]
print(p_fruits)

