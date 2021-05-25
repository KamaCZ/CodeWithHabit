# map function


def fahrenheit(celsius):
    return (9/5) * celsius  + 32

temps = [-10,0,5,20,30]

F_temps = map(fahrenheit, temps)

print(list(F_temps))


# map function with lambda function

print(list(map(lambda x: (9/5) * x + 32, temps)))

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

print(list(map(lambda x,y: x + y, a, b)))

