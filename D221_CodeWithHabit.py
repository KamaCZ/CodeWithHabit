# List comprehensions exercise
# create list of integers from 0 to n given n

n = int(input("Enter any integer > 0: "))

list_integers = [number for number in range(n+1)]
print(list_integers)