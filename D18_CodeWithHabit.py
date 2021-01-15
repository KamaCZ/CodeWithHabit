# List Comprehensions
# list comprehensions provide a concise way to create lists
# a list comprehension consists of brackets containing en expression followed by a for clause, then zero or more for or if clauses


squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

compr = [x**2 for x in range(10)]
print(compr)

squares = []
for x in range(10):
    if x != 5:
        squares.append(x**2)  
print(squares)

compr1 = [x**2 for x in range(10) if x != 5]
print(compr1)