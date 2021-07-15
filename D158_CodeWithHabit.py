# assignement: Create a function that will check if the string is a czech phone number or not. 
# This time dont use regular expressions
# The outcome is True or False

# examples of the czech phone numbers:
    # +420730149491
    # +420 730 149 491
    # 00420730149491
    # 730149491
    # 730 149 491


# "and" operator returns True if both statements are True
# "or" operator returns True if one of the statements is True

def isphonenumber(text):
    if len(text) != 13 and len(text) != 16 and len(text) != 14 and len(text) != 9 and len(text) != 11:
        return False # this cant be a czech phone number
    for i in range(len(text)):
        if not text[i].isdecimal() and text[0] != "+":
            return False

print(isphonenumber("+420730149491"))

