import re

phoneNum = "+420730 149491"

phoneReg = re.compile(r"\+\d\d\d\d\d\d\s\d\d\d\d\d\d")

print(phoneReg.findall(phoneNum))


