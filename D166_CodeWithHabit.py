import re

kamRegex = re.compile(r"kam(|il|a|ča|ilek)")
print(kamRegex.findall("Kama is nickname, but Kamil is name. Kamilek is a small Kamil and Kamča is like czech nickname."))
