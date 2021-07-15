# generators
# using the "yield" statement
# generators allow us to generate as we going along instead of holding everything in memory



def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)


# tomorrow recode the gencubes function so that it uses return statement, think about the difference