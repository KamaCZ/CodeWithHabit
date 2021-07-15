import re

name = "First Name: Kamil, Last Name: Klemsa"

nameRegex = re.compile(r"First Name: (.*), Last Name: (.*)")

print(nameRegex.findall(name))

