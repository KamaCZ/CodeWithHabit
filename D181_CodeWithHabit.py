import re

phoneNum = "420730149491"

phoneRegex = re.compile(r"\d\d\d\d\d\d\d\d\d\d\d\d")

print(phoneRegex.findall(phoneNum))


# Check the bugs tomorrow




