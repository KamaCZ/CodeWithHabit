# Inheritance
# way to create new classes by using already created classes

# creating a base class
class Animal():

    def __init__(self,name):
        self.name = name
        print("New animal created")


    def who_am_I(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal("Hugo")
myanimal.who_am_I()
myanimal.eat()

# creating a derived class
class Dog(Animal):

    def __init__(self,name):

        Animal.__init__(self,name)
        self.name = name
        print(f"I am a dog called {self.name}")

    # overwriting a function
    def who_am_I(self):
        print("I am a dog")   

my_dog = Dog("fido")
my_dog.who_am_I()
my_dog.eat()



