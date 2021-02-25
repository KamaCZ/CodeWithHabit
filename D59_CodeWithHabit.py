def check_even(num):
    return num % 2 == 0

print(check_even(110))


# check if any of the numbers in the list is even

def check_even_list(lst):
    for num in lst:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

lst1 = [5,99,3,2]
result = check_even_list(lst1)
print(result)


# make a function that returns all the even number in a list

lst1 = [1,2,5,10,11,100,105,1000,1001]
even_numbers = []

def all_even(lst):
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

print(all_even(lst1))

# tuples unpacking
# we can loop through the list of tuples and unpack them

stock_prices = [("AAPL", 130), ("GOOG", 1500), ("HON", 205)]


for item in stock_prices:
    print(item)

for stock,price in stock_prices:
    print(stock)
    print(price)
    print()



