import re

email = "kamil.klemsa@seznam.cz"

emailReg = re.compile(r"[a-zA-Z0-9._]+@[a-zA-Z0-9._]+")

print(emailReg.findall(email))