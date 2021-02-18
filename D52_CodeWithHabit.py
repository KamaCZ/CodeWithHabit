# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

[print(word) for word in st.split() if word[0] == "s"]


# Use range() to print all the even numbers from 0 to 10.

[print(x) for x in range(0,11) if x % 2 == 0]
# or:
print(list(range(0,11,2)))


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

lst = [x for x in range(1,51) if x % 3 == 0]
print(lst)


# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

print(st.split())
print(len(st.split()))

for word in st.split():
    if len(word) % 2 == 0:
        print(word,"- even")
    else:
        print(word, "- not even")
print()


[print("even") for word in st.split() if len(word) % 2 ==0]

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
#  and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

lst = [word[0] for word in st.split()]
print(lst)

    
    








