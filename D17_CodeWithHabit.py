# Dictionaries (basics)
# We can index themy by their keys
# They are formed with pairs. Each pair consists of a key and a value. They are separated by ":"
d = {"monday": ["1st", "MON", "checking e-mails"], "tuesday": ["2nd", "TUE", "strategy creation"]}
print(d)
print(d["tuesday"][1])
# keys can be only immutable data types: strings, numbers, tuples (in case they don`t consist of any mutable parts)
print("monday" in d) # checking if a key is inside the dictionary
del(d["monday"]) # deleting a key
print(d)
print()
d["wednesday"] = ["3rd", "WED", "pubbing"]
print(list(d)) # list of keys
print(sorted(d)) # getting sorted list of keys

d["wednesday"][2] = "drinking" # changing values 
print(d)
