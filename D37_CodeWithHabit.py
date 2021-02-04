# Advanced - numbers, strings etc.add()

# Floating point numbers (decimals)
float = 4E2
print(float)
float1 = -4E6
print(float1)

# Floor division
floor = 7 // 4
print(floor)

# Modulo
modulo = 7 % 4
print(modulo)

# Powers
power = 2 ** 3
print(power)

# Roots
root = 4 ** 0.5
print(root)

# Basic rules for variables (PEP8 rules)

# Dynamic typing in Python
# Python uses dynamic typing, meaning you can reassign variables to different datatypes.
dogs = 2
dogs = ["Fred", "Bob"]
print(dogs)

# Reassigning variable trick
a = 100
a = a + 100
print(a)

b = 100
b += 100
print(b)

# Strings
# using "\n" as a new line in code
print("Good morning")
print()
print("Bye Bye \n\n")
print("Good afternoon \n")
print("Good Bye")

# Indexing and slicing of strings
sentence = "Kamil Klemsa is the best Python Developer in the world" # Nooo I am not :) but working on that haha
name = sentence[:12]
profession = sentence[25:42]
print(name)
print(profession)
# negative slicing
profession = sentence[25:-13]
print(profession)

name = "Kama Klemsa"
# getting last letter
last = name[-1] # -1 means one index before index 0, which is the last letter of a string
print(last)
name_backwards = name[::-1] # last number "-1" means a leap, "-2" would mean that the program grabs any second letter
print(name_backwards)


