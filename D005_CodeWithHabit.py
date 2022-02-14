# for loop rewriting into while loop
# assignment: 
# print your name with a number behind the name starting with the number 5 going down up to number 1 
# 1) using for loop
# 2) using while loop

# for loop
for i in range(5,0,-1):
    print("Kamil " + str(i))

print("for_loop vs. while_loop")

i = 5
while 0 < i < 6:
    print("Kamil " + str(i))
    i = i -1
