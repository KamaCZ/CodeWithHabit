# Formatted string litterals (f-strings)
# example:
name = "Kamil"
print(f"My name is {name}.")
# use "!r" to give the string representation, meaning "wordexample"
print(f"He said, his name is {name!r}")

# float formatting 
# {value:{width}.{precision}}
result = 100.346677788766677
print(result)
print(f"The result of the operation1 is: {result:{10}.{5}}")
result2 = 120.2
print(f"The result of the operation2 is: {result2:10.2f}") # if we need more decimals we must use ".format()" formatting with f-strings

# alligning with f-strings litterals
print(f"The result of the operation2 is: {result2:<10.2f}") 
print(f"The result of the operation2 is: {result2:^10.2f}") 
print(f"The result of the operation2 is: {result2:>10.2f}") 

# more info on formatted string litterals:
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

# creating a formatted table of numbers
n1 = 33.582
n2 = 103.4
n3 = 155.14345645643564
n10 = 2.356334
n20 = 15
n30 = -0.3356676
print(f"{n1} | {n2} | {n3}")
print(f"{n10} | {n20} | {n30}")
print()
print(f"{n1:<7.2f} | {n2:^7.2f} | {n3:>7.2f}")
print(f"{n10:<7.2f} | {n20:^7.2f} | {n30:>7.2f}")











