# Dictionaries - for loops

dict = {"k1": 58, "k2": 65, "k3": 85}

# here only keys will be printed
for item in dict:
    print(item)

# here values will be printed
for item in dict.values():
    print(item)

# here both keys and values will be printed
for x,y in dict.items():
    print(x, "vs", y)

# getting a list from values or keys
print(dict.values())
l1 = dict.values()
print(l1)
print(type(l1))
l2 = list(l1)
print(l2)
print(type(l2))


