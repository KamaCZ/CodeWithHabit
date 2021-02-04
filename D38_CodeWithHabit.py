# concatenating strings
name = "Kama Klemsa"
say_hello = ("Hello " + name + " :)")
print(say_hello)

# multiplicating strings
name100Times = name * 100
print(name100Times)


# basic string methods

print(name.lower())
print(name.upper())
print(name.split())
print(name.split("a"))

# print formatting
# more about 
weather = "Today is a {}".format("beautiful") + " weather"
print(weather)


# string formatting
# Old versions: 
# 1) string formatting with placeholders (%s)
print("I am going to inject %s here and %s here." %("something", "as well"))
# 2) string formatting with the ".format{}" method
print("I am going to inject {0} here and {1} here.".format("something", "as well"))
# New version from python 3.6:
# Formatted string litterals (f-strings)
first = "something"
second = "as well"
print(f"I am going to inject {first} here and {second} here.")



