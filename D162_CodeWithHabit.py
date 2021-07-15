import re

text = "Hello World! is the title of the most programs in the world. Have you ever programmed any Hello World! program? Yes Hello World! program."


startEndReg = re.compile("Hello World!")

print(startEndReg.findall(text))


number = "45661348900"

startEndReg = re.compile(r"^\d+$")

print(startEndReg.findall(number))

