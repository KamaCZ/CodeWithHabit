import re
import pyperclip

email = pyperclip.paste()

emailReg = re.compile(r"[a-zA-Z0-9._]+@[a-zA-Z0-9._]+")

print(emailReg.findall(email))

