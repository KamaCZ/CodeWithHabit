# zip function
# can create a list from two separate lists
# the result will be list of tuples, each tuple will consist of two items - one from the first list, 
# another from the second list

l_letters = list(enumerate("Kamil Klemsa"))
print(l_letters)

for index,letter in l_letters:
    print(index+1,":",letter)


list_1 = list(range(1,101))
list_2 = list(range(101,201))
list_3 = list(zip(list_1,list_2))
print(list_3)

for x,y in list_3:
    print(x, "vs", y, end=", ")
print()
print(max(list_1))
print(min(list_2))




