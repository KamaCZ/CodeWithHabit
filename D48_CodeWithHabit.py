# while loops

x = 0
while x <=10:
    print("'x' is currently: " , x)
    print("'x' is still less than 10, adding 1 to 'x'")
    x += 1 # in case you forget to write this line of code, you will get the infinite loop and you'll need to stop it by pressing: F5, cntr+F5, fn+cntl+F5 or use built-in terminator on console

# break, continue, pass statements

# break statement = breaks out of the current closest enclosing loop
x = 0
while x <=10:
    print("'x' is currently: " , x)
    print("'x' is still less than 10, adding 1 to 'x'")
    x += 1
    if x == 4:
        break


# continue statement = goes to the top of the closest enclosing loop
odd100 = []
for num in range(101):
    if num % 2 == 0:
        continue
    odd100.append(num)
print("this is the list of odd numbers from 0 to 100:\n", odd100)













