import re
import pyperclip

text = pyperclip.paste()

phoneReg = re.compile(r"\d\d\d\d\d\d\d\d\d")

print(phoneReg.findall(text))
