# Finding out number of occurences of letters in a sentence.

sentence = "Kamil is one of the best Python Developers I personally know."
# In case we need only a specific letter occurence such as "a":
print(sentence.count("a"))

# In case we want occurences of all the letters:
import re
regex = re.compile(r'[a-zA-Z]', re.I) # creating a regex object
found = re.findall(regex, sentence) # using findall method to find out all occurences of the regex object
print(found)

import collections
occurences = collections.Counter(found) # creating a dictionaries with the numbers of occurences for all the letters
print(occurences)

for key, value in occurences.items(): # for loop that will print out occurences of all the letters
    print(key + ": " +str(value))
    print(key,":",value)


#ideas for making it better: think about how to make it case insensitive, i.e. I and i is counted together
# ideas: think about other ways how to solve this problem

