import re

text = "<this is tag> inside another tag>"

nonGreedy = re.compile(r"<(.*?)>")
print(nonGreedy.findall(text))

greedy = re.compile(r"<(.*)>")
print(greedy.findall(text))