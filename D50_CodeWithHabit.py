# difference between "pass" and "return" statements
# pass is an empty statement and if there is more code after this statement it wil be executed
# return returns the value and the next bunch of code in the function will not be executed

def f(num):
    if num > 2:
        print(num)
    return
    if num <=2:
        print("This will not be printed if num<=2")

f(2)

def f(num):
    if num > 2:
        print(num)
    pass
    if num <=2:
        print("This will be printed if num<=2")

f(2)

# OTHER Useful Operators
# 1) enumerate
# enumerate is very useful function to use with for loops
# we use it when we need to count the index

index_count = 0

for letter in "Kamil Klemsa":
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1


for i, letter in enumerate("Kamil Klemsa"):
    print("At index {} the letter is: {}".format(i, letter))

print(enumerate("Kamil Klemsa"))
print(list(enumerate("Kamil Klemsa")))
print()

# zip function
# in the above case when we use enumerate and pass it to the "list" function we get list of tuples
# we can go the other way round - if we have several lists we can use "Zip" function to create list of tuples

l1 = [1,2,3,4,5,6,7,8,9,10,11,12]
l2 = ["K","a","m","i","l"," ","K","l","e","m","s","a"]
print(list(zip(l1,l2)))

for item1,item2 in list(zip(l1,l2)):
    print("For this tuple, first item was {} and the second item was {}".format(item1,item2))