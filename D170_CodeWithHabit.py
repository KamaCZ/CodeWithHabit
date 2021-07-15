import re

text = "Name: Kamil Name: Luboš"


nameRegex = re.compile(r"Name: (.*)")

print(nameRegex.findall(text))


# check it later