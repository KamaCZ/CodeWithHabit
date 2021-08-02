import re

phoneNum = "420730149491"

phoneReg = re.compile(r"\d\d\d\d\d\d\d\d\d\d\d\d")

print(phoneReg.findall(phoneNum))