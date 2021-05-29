# Zip function

lst1 = [1,2,3,4]
lst2 = [5,6,7]
print(list(zip(lst1,lst2)))

dict1 = {"a": 1,"e": 7}
dict2 = {"b": 3,"f": 8}
dict3 = {"c":5,"g": 10}
print(list(zip(dict1, dict2, dict3)))

print(list(zip(dict1.values(), dict2, dict3)))