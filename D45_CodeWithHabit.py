# Python uses file objects to interact with the files on your computer
# These files can be of any sort, either it is an audio file, text, email, microsoft documents
# certain libraries need to be installed to interact with certain file types

# Python has built in open function to enable interact with basic files like "txt" files
file = open("myFile.txt", "w+") # "w+" opens the file for reading and writing, rewrites the original document"

file.write("Today is thursday, 10th of February 2022")
file.seek(0) # returns the cursor at the beginning of the text, so the program can read the text
print(file.read()) # this code will end up with error message, program can`t read it because it is in the write mode
file.close()

file = open("myFile.txt", "a+") # using "w" will rewrite the original file
file.write("And covid-19 is still here.\n Tomorrow is Friday\n and my name is Kama babe")
file.close()

file = open("myFile.txt")
print(file.read())
print()
file.seek(0) # it will return cursor to the first line so that if you want to call read function again it will read the document, otherwise it returns ""
file.close()

# check it tomorrow

file = open("myFile.txt")
print(file.readline()) # will read the first line
print(file.readline()) # will read the second line
file.close()




