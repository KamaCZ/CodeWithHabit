class Dog:

    species = "mammals"

    def __init__(self,breed,name,spots):
        # we are passing the argument to the name of the specifi instance of the Dog class 
        # the name of the instance is "breed"
        # you can as well have the name e.g. my_breed and the argument = breed, but the convence is
        #  to have all names same
        self.breed = breed
        self.name = name
        self.spots = spots
    # you can allow the method to take in more arguments to pass when you call it
    def bark(self,number):
        print(f"Wooof. My name is {self.name}. My number is {number}")


dog1 = Dog("Lab","Fido",True)

print(dog1.breed)
print(dog1.name)
print(dog1.species)
print(dog1.spots)
dog1.bark(5)






