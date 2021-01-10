# Working with list, we can use list to create a graphical sequences of numbers
# Using, indexin, slicing

digits = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in range(len(digits)):
    print("index: " +str(i) + " digit: " + str(digits[i]))
print()

"""
We want to create the following sequence:
[]
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
for i in range(len(digits)):
    print(digits[:i])
print()

"""
We want to create this:
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]
[4, 5, 6]
[5, 6, 7]
[6, 7, 8]
[7, 8, 9]
[8, 9, 10]
"""
for i in range(len(digits)-3):
    print(digits[i:i+3])
print()

"""
The same assignment as above, but we gonna create it programatically 'correct'.
"""
window_size = 3
for i in range(len(digits)-window_size):
    print(digits[i:i + window_size])
print()

# The same assignment, but we are increasing the window size to 5
window_size = 5
for i in range(len(digits)-window_size):
    print(digits[i:i + window_size])
print()






