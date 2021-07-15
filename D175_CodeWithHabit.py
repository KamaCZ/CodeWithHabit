import re

batRegex = re.compile(r"bat(man|mobile|tog|race")

print(batRegex.search("batman is looking for a batmobile"))

# check it tomorrow