# Code takes in any integer from 1 to 150
# Without using any string methods, try to print the following:
# 123....n

# Note that "..." represents the consecutive values in between.
# Example 
# n=5
# Print the string 12345

n = int(input("Enter any integer from 1 to 150: "))

for i in range(n):
    print(i+1, end="")


