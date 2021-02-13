l = [1,2,3,4,5,6,7,8,9,10]

sum = 0
for num in l:
    sum += num
print(sum)

# with for loops you can iterate through lists, string, dictionaries, tuples, sets

string = "Today is a beautiful day"
dictionary = {"key1": "value1", "key2": "value2"}
tuple = (100,200,300,400,500)
set = {1,100,2,200,3,300}

for letter in string:
    print(letter * 3)

for item in dictionary:
    print(item)

for item in tuple:
    print(item / 2)

sum = 0
for item in set:
    sum += item

print(sum)


