# Dictionaries
dict = {1: "apple", "key1": "8"}
print(dict["key1"])

# adding into an empty dictionay
d = {}
d[1] = "apple"
print(d)

# nesting with dictionaries
keys = {"key1": {"subkey": {"2subkey": "58"}}}
print(keys)
print(keys["key1"]["subkey"]["2subkey"])

# dictionary methods
print(dict.keys())
print(dict.values())
print(dict.items())