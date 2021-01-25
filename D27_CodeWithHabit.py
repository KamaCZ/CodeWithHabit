# 2D lists = Nested lists
# Nested lists can represent tables

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid:
    print(row)


for row in number_grid:
    for column in row:
        print(column)
    