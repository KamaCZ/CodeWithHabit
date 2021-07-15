import re
import smtplib

numbers = "1234565434445 a 1"

numReg = re.compile(r"^\d+$")

mo = numReg.search(numbers)
print(mo)

mo1= numReg.findall(numbers)
print(mo1)


emailAddresses = "kama.klemsa@gmail.com a kamil.klemsa@seznam.cz"

domainReg = re.compile(r".com")

mo = domainReg.findall(emailAddresses)

print(mo)

