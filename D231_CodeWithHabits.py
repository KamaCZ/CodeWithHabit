# Tuple unpacking 
# through tuple unpacking we can access individually items that are inside a tuple

l2 = [(1,2),(5,10),(8,52)]

for (t1,t2) in l2:
    print(t1,t2)


for (t1,t2) in l2:
    print(t1)


t2 = ((1,2),(5,10),(8,52))

for (t1,t2) in t2:
    print(t1)