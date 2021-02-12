# chained comparison operators

print(1 < 3 < 2)
# or:
print(1 < 2 and 3 < 2)

print(1 < 2 or 3 < 2) # one of the values needs to be true

# if, elif, else statements exercise:
a = 4
b = 2
if a > b:
    a = 2
    b = 4
    print(a,b)
elif a == b:
    print(a,b)
else:
    print("'a' was less than 'b'") 


# for loops exercises:
# printing only even numbers from a list of numbers:

l = [1,2,3,4,5,6,7,8,9,10]
for num in l:
    if num % 2:
        print(num)
    else:
        print("This is an odd number")




