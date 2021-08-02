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


phoneRegex = re.compile(r"")