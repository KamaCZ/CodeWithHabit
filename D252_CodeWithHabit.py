# Polymorphism - we have different classes, and the same method name for all of them
# then we can call the method from one place

class Dog():
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + " says woooof")

class Cat():
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + " says moewwww")

my_dog = Dog("Fido")
my_dog.speak()

my_cat = Cat("Mourek")
my_cat.speak()

# with creation of a new function
def general_speak(animal):
    animal.speak()

general_speak(my_dog)
general_speak(my_cat)

# with for loop
for animal in [my_dog,my_cat]:
    animal.speak()






    