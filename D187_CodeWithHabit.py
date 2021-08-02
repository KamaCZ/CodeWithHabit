import re

phoneNumber = "+420 730 149491 and +420 730149491"

phoneRegex = re.compile(r"(\+\d\d\d\s\d\d\d)(\s)?(\d\d\d\d\d\d)")

print(phoneRegex.findall(phoneNumber))


# check tomorrow