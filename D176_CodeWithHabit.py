import re

batRegex = re.compile(r"bat(man|woman|men|women)")

text = ("A batwoman killed a batman, and then all batwomen killed all batmen")

mo = batRegex.search(text)
print(mo)
print()
print(mo.group())


mo = batRegex.findall(text)
print(mo)

