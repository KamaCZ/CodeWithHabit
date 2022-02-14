# Files

# checking the current location of the terminal
import os
print(os.getcwd())
os.chdir("/Users/kama/PYTHON/COURSES/UDEMY_FROM_ZERO_TO_HERO/Complete-Python-3-Bootcamp-master_working_version")
print(os.getcwd())

# creating a new text file in a specific location
# my_file = open("/Users/kama/PYTHON/COURSES/UDEMY_FROM_ZERO_TO_HERO/Complete-Python-3-Bootcamp-master_working_version/text_file.txt","w")
my_file = open("text_file.txt","w+")
# w - for writing
# w+ - for writing and reading
# a+ - append and read

# writing to a txt file:
my_file.write("Today is a beautiful day")
my_file.seek(0)
print(my_file.read())
print()
my_file.seek(0)
print(my_file.read())
my_file.close()

print(os.getcwd())

my_file = open("text_file.txt","a+")

my_file.write("\nThis is another line of the file")
my_file.seek(0)
print(my_file.read())
my_file.close()








