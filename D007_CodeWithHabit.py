# Encrypted language

"""
Assignment: create an encrypting language translator. The rules for encryption will be as follows:
Letter "a" will be "1"
Letter "z" will be "26"
"." will be "0"
" " will be "."
"," will be "L"
"0" will be "a"
"9" will be "j"
other letters and signs will stay as they are!
create a function that takes in the phrase as an parameter
"""

def translator(phrase):
    translated_phrase = ""
    for letter in phrase:
        if letter == "a":
            translated_phrase += "1"
        elif letter == "z":
            translated_phrase += "26"
        elif letter == ".":
            translated_phrase += "0"
        elif letter == " ":
            translated_phrase += ","
        elif letter == "L":
            translated_phrase += "0"
        elif letter == "9":
            translated_phrase += "j"
        else:
            translated_phrase += letter
    print(translated_phrase)


translator("This is an example of a simple translator made in Python3.10")