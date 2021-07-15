import re

# using substitution with RE, method .sub()
# RE.i performs case insensitive matching
nameRegex = re.compile(r"Agent \w+", re.I)
print(nameRegex.findall("Agent Bob met agent Kamil and they had threesome with Agent Fred"))  
print(nameRegex.sub("REDACTED","Agent Bob met agent Kamil and they had threesome with Agent Fred"))


