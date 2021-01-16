# Regex introduction
# regex is built-in module, we call it: import re
# the whole bunch of documentation: https://docs.python.org/3/library/re.html
# we use it to find our pre-defined patterns

sentence = "Today is a beautiful day. It is actually monday. Usually the best day for me is Friday or Saturday. Sunday is usually boring. What is your favourite day?"
# we need to find all days included in the sentence
# it can be monday, tuesday, friday, saturday, sunday, Monday, Tuesday, Wednesday, Thirsday, Friday, Saturday, Sunday

import re
day_regex = re.compile(r"\w+day")
results = day_regex.findall(sentence)
print(results)