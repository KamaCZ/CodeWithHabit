# Gaus numbers
# Assignement: 
# create for loop which makes total of all numbers 1-100: 1+2+3....+100

total = 0

for num in range(101):
    total = total + num

print(total)

# create a function that makes total of a number

def gaus(num):
    total = 0
    for x in range(num):
        total = total + (x+1)
    print(total)

gaus(100)
