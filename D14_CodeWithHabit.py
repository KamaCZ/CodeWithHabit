
habits = "cue, craving, response, reward"
hab = habits.split(", ")
print(hab)


habits2 = " and ".join(hab)
print(habits2)

# TUPLES
# tuples are data structures defined by ()
# tuples  are sequenced (can be indexed or sliced) and immutable data structures (can`t be changed)
# they are used when we are sure we will not want to change therm in future
# advantage is that they take less memory


person1 = ("Kamil Klemsa", 20, "Pythonist")
person2 = ("Milan Kvapil", 40, "Runner")
person3 = ("Tomáš Klemsa", 9, "Student")
print(person3[2])
print()
# person3[2] = "Pilot" - this is not possible, tuples are immutable

# Tuple unpacking
people = [person1, person2, person3]

for name, age, job in people:
    print(name)
    print(age)
    print(job)
    print()

# List unpacking, seeing the difference with tuples, because lists are mutable
person1 = ["Kamil Klemsa", 20, "Pythonist"]
person2 = ["Milan Kvapil", 40, "Runner"]
person3 = ["Tomáš Klemsa", 9, "Student"]

person3[2] = "Pilot"
people1 = [person1, person2, person3]
print(person3)
print()

for name, age, job in people1:
    print(name)
    print(age)
    print(job)
    print()





