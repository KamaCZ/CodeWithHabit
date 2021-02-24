# beginners usually write the code this way:
def even_check(number):
    result = number % 2 == 0
    return result

print(even_check(20))
print(even_check(21))

# advanced write it this way:
def even_check(number):
    return number % 2 == 0

print(even_check(20))
print(even_check(21))

# function that returns true if any number is "even" inside a list
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True # return statement break out of the for loop
        else:
            pass # pass is null statement, it will do nothing
    return False # it after checking all the numbers of the list the function does not find any even number it returns False

print(check_even_list([1,2,3]))
print(check_even_list([1,3,5]))