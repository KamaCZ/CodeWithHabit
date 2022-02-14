# String formatting with .format() method
# documentation: https://docs.python.org/3/library/string.html#formatstrings
# advantages compared to %s:


print("Here {} will be injected and another thing will be injected.".format("something"))

# 1) insterted objects can be called by index position:
print("{2} was first, {0} was second, and {1} was third.".format("John","Fred","Tonny"))

# 2) inserted objects can be assigned keywords:
print("First object:\t{a}\nSecond Object:\t{b}\nThird Object:\t{c}".format(b="Kamil",c=2,a=52.3))

# 3) inserted objects can be reused, avoiding duplication
print("Every {p} saved is every {p} saved.".format(p="penny"))


