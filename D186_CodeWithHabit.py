import re
import pyperclip

# create a phone regex for following forms of US phone numbers:
# 1) 315-250-1111
# 2)     250-1111
# 3) (315) 250-1111
# part of the phone number can be as well extension in the following forms:
# 1)     250-1111 ext 12345
# 2)     250-1111 ext. 12345
# 3)     250-1111 x12345


phoneRegex = re.compile(r"""
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)?                     # first separator
\d\d\d                      # first three digits
(\s|-)?                     # second separator
\d\d\d\d                    # last four digits
)                  
#(ext(\.)?\s)               # extension word part + number part
""")

print(phoneRegex.findall("315-250-1111"))


# check it tomorrow