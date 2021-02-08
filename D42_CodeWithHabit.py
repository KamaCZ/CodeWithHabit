# Tuple methods

t = (1,2,5,2,6,8,10,1)
print(t.index(1))
print(t.count(1))

# tuples are similar to lists, but they are immutable, you cannot change any objects inside neither to append or add 
# using tuples in case that you dont wont to change data in any way in future! Helps to integrity of data


# SETS = unordered collection of unique objects
# creating an empty set:
s = set()
print(s)
s.add("Monday")
print(s)

# creating a set with some objects 
s1 = {5,6,8,10}
print(s1)

# we can use sets when we want to get only unique objects from a list
l = [1,2,5,2,6,8,2,10,1]
print(set(l))
new_set = set(l)

for item in new_set:
    print(item)

# Booleans
# True - integer 1
# False - integer 0
# None = placeholder value for object we don`t want to reassign yet

a = True
b = 1 > 2
c = None
print(a,b,c)
