# Dictionaries - some additional stuff and exercises

# Dictionaries are really flexibale in terms of data types:
dict_example = {"Jose": {"age": 20, "height": 178, "weight": 75, "character": "friendly"}, "credit_cards": ["**** **** 5785", "**** **** 5735"]}
print(dict_example)

# methods can be used for a specific values of a dictionary
print(dict_example["Jose"]["character"].upper())

dict_example["Jose"]["age"] = 30

print(dict_example)

