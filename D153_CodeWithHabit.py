# generators 

# Create a generator that generates the squares of numbers up to some number N.

def squaregen(N):
    for i in range(N):
        yield i**2


for square in squaregen(10):
    print(square)
