import re

text = ("First Name: Kamil Last Name: Klemsa, First Name: Luboš Last Name: Klemsa")


nameRegex = re.compile(r"First Name: (.*), Last Name (.*)")

print(nameRegex.findall(text))


nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
print(nameRegex.findall("First Name: Al Last Name: Sweigart"))
