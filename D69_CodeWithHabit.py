"""
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""


def find_33(lst):
    for n in range(0, len(lst)-1):
        if lst[n] == 3 and lst[n+1] == 3:
            return True
    return False
    

print(find_33([1,3,3]))
print(find_33([1,3,1,3]))
print(find_33([3,1,3]))

def find_33(lst):
    for n in range(0, len(lst)-1):
        if lst[n:n+2] == [3,3]:
            return True
    return False
    

print(find_33([1,3,3]))
print(find_33([1,3,1,3]))
print(find_33([3,1,3]))




