import re
import pyperclip

email = pyperclip.paste()

emailRegex = re.compile(r"[a-zA-Z0-9._]+@[a-zA-Z0-9._]+")

print(emailRegex.findall(email))

my_sentence = "I love to learn new things"
splited = my_sentence.split()
x = splited[-1]
print(x)