# Encrypted language

"""
Assignment: create an encrypting language translator. The rules for encryption will be as follows:
Letter "a" will be "1"
............
Letter "z" will be "26"
"." will be "0"
" " will be "."
"," will be "O"
"0" will be "a"
.............
"9" will be "j"
anything other will be "-"
"""


def encryptor(phrase):
    translatedPhrase = ""
    for letter in phrase:
        if letter.lower() == "a":
            translatedPhrase = translatedPhrase + "1"
        elif letter.lower() == "z":
            translatedPhrase = translatedPhrase + "27"
        elif letter == ".":
            translatedPhrase = translatedPhrase + "0"
        elif letter == ",":
            translatedPhrase = translatedPhrase + "O"
        elif letter == "0":
            translatedPhrase = translatedPhrase + "a"
        elif letter == "g":
            translatedPhrase = translatedPhrase + "j"
        else:
            translatedPhrase = translatedPhrase + "-"
    return translatedPhrase

print(encryptor(input("enter the text to be translated: ")))
