import re

text = "Hello world! Hello world!"

endWithWorldReg = re.compile(r"!$")
print(endWithWorldReg.findall(text))

