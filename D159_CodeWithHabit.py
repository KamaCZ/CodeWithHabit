import re

message = "Call me 730149491, 733108509 or +420730149491"

czePhoneRegex = re.compile(r"\d\d\d\d\d\d\d\d\d | \+\d\d\d\d\d\d\d\d\d\d\d\d\d")

regobj = czePhoneRegex.search(message)

print(regobj.group())

print(czePhoneRegex.findall(message))

#check again tomorrow