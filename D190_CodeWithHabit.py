import re

extension = "ext.1234 or x1234"

extRegex = re.compile(r"ext(\.)?\d\d\d\d")

print(extRegex.findall(extension))

# check tomorrow

