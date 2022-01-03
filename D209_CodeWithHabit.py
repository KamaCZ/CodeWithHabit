import re
import pyperclip

phoneNumber = pyperclip.paste()

phoneReg = re.compile(r"\+\d\d\d\d\d\d\d\d\d\d\d\d")


print(phoneReg.findall(phoneNumber))

