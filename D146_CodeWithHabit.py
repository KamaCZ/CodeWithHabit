# reduce() function
# similar to map function, has as well two arguments, one is a function, one a list
# difference is that at first the function applies to the first two objects of the list, and in another step 
# it applies to the result of this operation and the next object in the list
# result is one value

from functools import reduce


lst = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,lst))