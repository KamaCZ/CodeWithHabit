# using () in case the () are the part of RE

import re

myNumber = +420730149491

phoneNumReg = re.compile(r"((+\d\d\d)(\d\d\d\d\d\d\d\d\d))")

print(phoneNumReg.findall(myNumber))


# check this tomorrow
