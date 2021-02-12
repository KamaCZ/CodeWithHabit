# Python uses file objects to interact with the files on your computer
# These files can be of any sort, either it is an audio file, text, email, microsoft documents
# certain libraries need to be installed to interact with certain file types

# Python has built in open function to enable interact with basic files like "txt" files
file = open("myFile.txt", "w+") # "w+" opens the file for reading and writing, rewrites the original document"

file.write("Today is thursday, 10th of February 2022\n\n")
#print(file.read()) 
file.close()

file = open("myFile.txt", "a+") # adds text behind the current text
file.write("And covid-19 is still here.\nTomorrow is Friday\nand my name is Kama babe")
file.close()

file = open("myFile.txt")
print(file.read())
print()
file.close()


file = open("myFile.txt")
print(file.readline()) # will read the first line
print(file.readline()) # will read the second line
file.close()

# itirating through a file:
for line in open("myFile.txt"):
    print(line)


