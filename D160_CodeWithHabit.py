import re

message = "Call me 730149491, 733108509"
czePhoneRegex = re.compile(r"\d\d\d\d\d\d\d\d\d") 
regobj = czePhoneRegex.findall(message)

print(regobj)


lst = ["Hello World", "the word Hello", "what is Hello?"]

startsWithHello = re.compile("^Hello")

obj1 = startsWithHello.findall(lst[0])

print(obj1)

# tomorrow try to make a for loop
