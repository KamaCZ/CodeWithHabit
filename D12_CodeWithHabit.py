# Working with strings

# Situtation when we have a string and we want to get all the words separated into the single words.

# We have to options:
# 1) using "split()" method (in case string doesn't contain other symbols)
# 2) using "findall()" method of "regex" module (in case the string containts other symbols)

# 1)
txt = "Today it is winter january the 9th Saturday 2021 and it is a lot of snow around and it is freezing"
x = txt.split()
print(x)

# 2)
import re # importing regex module
txt2 = "Today, it`s winter 9.1.2021, Saturday. It is a lot of snow around, and it is freezing :), omg!"
regex_word = re.findall(r"\w+", txt2) # creating a regex object (for words) and passing it to findall function
print(regex_word)
