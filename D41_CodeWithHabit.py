# Dictionaries - some additional stuff and exercises

# Dictionaries are really flexibale in terms of data types
# nesting dictionaries is very powerfull,  we can create dictionaries inside other dictionaries
dict_example = {"Jose": {"age": 20, "height": 178, "weight": 75, "character": "friendly"}, "credit_cards": ["**** **** 5785", "**** **** 5735"]}
print(dict_example)

# methods can be used for a specific values of a dictionary
print(dict_example["Jose"]["character"].upper())

dict_example["Jose"]["age"] = 30

print(dict_example)

# some dictionaries methods:

d = {"K1": 2021, "K2": 2, "K3": 8}
print(d)
print(d.keys())
print(list(d.keys()))
print(list(d.values()))
print(list(d.items())) # returns tuples of all items
items1 = d.items()
print(type(items1))


