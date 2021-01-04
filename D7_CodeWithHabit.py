# Encrypted language

"""
Assignment: create an encrypting language translator. The rules for encryption will be as follows:
Letter "a" will be "1"
............
Letter "z" will be "26"
"." will be "0.
" " will be "."
"," will be "O"
"0" will be "a"
.............
"9" will be "j"
anything other will be: "-"
"""

def encryption(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() == "a":
            translation = translation + "1" + "-"
        elif letter.lower() == "b":
            translation = translation + "2" + "-"
        elif letter.lower() == "c":
            translation = translation + "3" + "-"
        elif letter.lower() == "d":
            translation = translation + "4" + "-"
        elif letter.lower() == "e":
            translation = translation + "5" + "-"
        elif letter.lower() == "f":
            translation = translation + "6" + "-"
        elif letter.lower() == "g":
            translation = translation + "7" + "-"
        elif letter.lower() == "h":
            translation = translation + "8" + "-"
        elif letter.lower() == "i":
            translation = translation + "9" + "-"
        elif letter.lower() == "j":
            translation = translation + "10" + "-"
        elif letter.lower() == "k":
            translation = translation + "11" + "-"
        elif letter.lower() == "l":
            translation = translation + "12" + "-"
        elif letter.lower() == "m":
            translation = translation + "13" + "-"
        elif letter.lower() == "n":
            translation = translation + "14" + "-"
        elif letter.lower() == "o":
            translation = translation + "15" + "-"
        elif letter.lower() == "p":
            translation = translation + "16" + "-"
        elif letter.lower() == "q":
            translation = translation + "17" + "-"
        elif letter.lower() == "r":
            translation = translation + "18" + "-"
        elif letter.lower() == "s":
            translation = translation + "19" + "-"
        elif letter.lower() == "t":
            translation = translation + "20" + "-"
        elif letter.lower() == "u":
            translation = translation + "21" + "-"
        elif letter.lower() == "v":
            translation = translation + "22" + "-"
        elif letter.lower() == "w":
            translation = translation + "23" + "-"
        elif letter.lower() == "x":
            translation = translation + "24" + "-"
        elif letter.lower() == "y":
            translation = translation + "25" + "-"
        elif letter.lower() == "z":
            translation = translation + "26" + "-"
        elif letter.lower() == "0":
            translation = translation + "a" + "-"
        elif letter.lower() == "1":
            translation = translation + "b" + "-"
        elif letter.lower() == "2":
            translation = translation + "c" + "-"
        elif letter.lower() == "3":
            translation = translation + "d" + "-"
        elif letter.lower() == "4":
            translation = translation + "e" + "-"
        elif letter.lower() == "5":
            translation = translation + "f" + "-"
        elif letter.lower() == "6":
            translation = translation + "g" + "-"
        elif letter.lower() == "7":
            translation = translation + "h" + "-"
        elif letter.lower() == "8":
            translation = translation + "i" + "-"
        elif letter.lower() == "9":
            translation = translation + "j" + "-"
        elif letter.lower() == ".":
            translation = translation + "0" + "-"
        elif letter.lower() == ",":
            translation = translation + "O" + "-"
        elif letter.lower() == " ":
            translation = translation + "."  + "-"   
        else:
            translation = translation + "_" + "-"
    return translation

print(encryption(input("Please enter the text to be translated: ")))




