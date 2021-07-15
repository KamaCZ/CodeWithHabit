# all() and any() functions
# all() returns True if all the items in the iterrable are True
# any() returns True if one of the items in the iterrable is True

lst = [len("kamil") > 3, False]

print(lst)

print(all(lst))

print(any(lst))