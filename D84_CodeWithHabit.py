# function exercises

# Write a function that computes the volume of a sphere given its radius.

def volume(rad):
    return (4/3) * 3.14 * rad**3


print(volume(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def in_between(min,max,num):
    return num >= min and num <=max

print(in_between(1,10,15))

# or:
def in_between(min,max,num):
     return num in range(min,max+1)

print(in_between(1,10,10))

# or:

def in_between(min,max,num):
    if num in range(min,max+1):
        print("{} is in range between {} and {}".format(num,min,max))
    else:
        print("{} is out of the range.".format(num))

print()
in_between(1,10,10)
in_between(1,10,11)