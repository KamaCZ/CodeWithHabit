# Strings formatting
# Documentation: https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# 1) String formatting operator: "%s"
# 2) .format() method
# 3) formatting string litterals(f-strings)

# 1) %s
word = "something"

print("I am going to inject %s here." %word)

print("I am going to place %s here and %s here." %(word,word))

print("This is %s awesome." %"fucking")

# 1) %r - converts strings including "",\t, \n, etc.
print("He said his name was %r." %"Kamil")
print("He said his name was %s." %"Kamil")

print("I once caught a fish. This %s." %"\tbig")
print("I once caught a fish. This %r." %"\tbig")

# 1) %d - converts numbers into integers without formatting
print("I got %s CZK" %3.75)
print("I got %d CZK" %3.75)






