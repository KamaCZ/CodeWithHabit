import re

phoneNum = "+420 730149491 or +420730149491"

phoneRegex = re.compile(r"(\+\d\d\d(\s)?\d\d\d\d\d\d\d\d\d)")


print(phoneRegex.findall(phoneNum))
