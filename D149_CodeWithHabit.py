# enumerate function
# allows you to keep a count when you iterate through an object
# it creates tuples, pass it to the list!

months = ["january","february","march","april"]

enumerated = enumerate(months,start=1)

for number,month in enumerated:
    print(number, month)


lst = ["a","b","c"]

print(list(enumerate(lst)))

for number,item in enumerate(lst):
    if number >= 2:
        break
    else:
        print(item)




