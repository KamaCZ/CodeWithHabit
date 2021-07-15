import re

text = "First Name: Kamil Last Name: Klemsa First Name: Kamil Last Name: Klemsa"
print()

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")

print(nameRegex.findall(text))

serve = "<To serve humans> for dinner.>"

nongreedy = re.compile(r"<(.*?>)")
print(nongreedy.findall(serve))

greedy = re.compile(r"<(.*)>")
print(greedy.findall(serve))
