import re

phrase = "Kamil is Kama."

regex = re.compile(r".{1,10}m")

print(regex.findall(phrase))