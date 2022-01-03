import re

text = "20% is more than 80%"

print(text)

percentReg = re.compile(r"%|\d+%")

print(percentReg.findall(text))


