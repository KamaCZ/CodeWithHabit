class Person:

    def __init__(self, name, age, location, distance):
         
         self.name = name
         self.age = age
         self.location = location
         self.distance = distance

    
person1 = Person("Kamil", 29, "Mosjoen", 12000)

print(person1.distance)