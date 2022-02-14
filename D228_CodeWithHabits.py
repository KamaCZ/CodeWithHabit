name_letters = [x for x in "Kamil Klemsa"]
print(name_letters)
print(len(name_letters))


print(len([x for x in range(1,1000001) if x % 100 == 0]))

# create a function that transfers celsius into fahrenheit, 
# list of celsius temperatures will be passed as an argument
# use list comprehensions

def fahrenheit(list_celsius):
    return [x*9/5+32 for x in list_celsius]

print(fahrenheit([-50,-10,0,10,15,20,25,30,40,50]))

# create a list containing numbers to the power of two made out of another list of numbers
# containing numbers to the power of two made out of numbers in a range from 1 to 100
# but only those that are odd

print([x**2 for x in[x**2 for x in range(1,101) if x % 2 == 1]])
print(len([x**2 for x in[x**2 for x in range(1,101) if x % 2 == 1]]))






