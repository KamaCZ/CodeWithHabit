# creating an abstract class, that is never supposed to be instantiated
class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

# calling the method will raise the error:
# my_animal = Animal("Fred")
# print(my_animal.name)
# my_animal.speak()

class Dog(Animal):

    def speak(self):
        return self.name + " says Woof!"

my_dog = Dog("Fido")
print(my_dog.name)
print(my_dog.speak())


class Cat(Animal):

    def speak(self):
        return self.name + " says Moewww!"

my_cat = Cat("Mourek")
print(my_cat.name)
print(my_cat.speak())


