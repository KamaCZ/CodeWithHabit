import re
import pyperclip

emails = pyperclip.paste()

emailReg = re.compile(r"[a-zA-Z0-9._+]+@[a-zA-Z0-9._+]+")

print(emailReg.findall(emails))



