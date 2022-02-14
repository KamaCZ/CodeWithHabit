# in loops we can use these statements that add additional functionality:
# pass - does nothing
# break - breaks out of the current closest enclosing loop
# continue - goes to the top of the closest enclosing loop

# pass is mostly used when we create functions and dont want to get an error statement
def my_func(num):
    pass

my_func(100)

# continue

names = ["Kamil","John","Fredy","Ben","Agnieszka"]
names_wo_a = []
for name in names:
    if "a" in name:
        continue
    names_wo_a.append(name)
print(names_wo_a)


# break
s1 = set(list(range(1,101)))
print(s1)

for x in s1:
    print(x)
    if x == 50:
        break
        

        
