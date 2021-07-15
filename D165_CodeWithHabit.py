import re

resume = """ Kamil phone numbers are: 582-356-4444 and 333-456-4444.
Kamil žije jako freelancer a můžete se mu také dovolat na telefonní číslo
do Norska:
 - 533-433-4644
 Děkuji
 S pozdravem
 KK
 """


phoneRegex = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")

mo1 = phoneRegex.search(resume)

mo2 = phoneRegex.findall(resume)

print(mo1)
print()
print(mo2)
print()
print()


print(mo1.group(0))
print(mo1.group(1))
print(mo1.group(2))
print(mo1.group(3))


