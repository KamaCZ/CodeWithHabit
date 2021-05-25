# map function


def fahrenheit(celsius):
    return (9/5) * celsius  + 32

temps = [-10,0,5,20,30]

F_temps = map(fahrenheit, temps)

print(list(F_temps))


