# SETS
# data type in Python
# they are not sequenced, unordered (we can`t index them or slice them)
# to create we use "set()" function passing it another data type, or entering objects between {}
# "sets" are sets of unigue objects (no duplicants)
# documentatiton: https://docs.python.org/3/tutorial/datastructures.html#sets
# main usage: eliminating of duplicate items, membership testing

set1 = {"black", "white", "green", "yellow", "white", "red", "black"}
print(set1)
print(type(set1))
set1.add("rosa")    # we can add object into a set
print(set1)
print()

set2 = set([25, 18, 1, 3, 8, 60, 3, 8, 25, 16, 38]) # creating set from a list
print(set2)

set3 = set1.union(set2) # joining two sets
print(set3)

common = set1.intersection(set2) # checking if there are some items contained in both sets
print(common)

diff1 = set1.difference(set2) # checking what items are missing in set2 compared to set1
print(diff1)

diff2 = set2.difference(set1) # checking what items are missing in set1 compared to set2
print(diff2)

