# filter function: filter(func, iterator)
# this function filter out all the elements of the iterable, for which the result of the function returns True 
# and the list of items will filtered out will be the result


def return_even(num):
    if num%2 == 0:
        return True

lst = range(1,21)
print(list(lst))


print(list(filter(return_even, lst)))


print(list(filter(lambda x: x%2==0, lst)))