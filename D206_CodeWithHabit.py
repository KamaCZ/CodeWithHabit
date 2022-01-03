class Hotel:

    def __init__(self, name, location, capacity, numEmployees):

        self.name = name
        self.location = location
        self.capacity = capacity
        self.numEmployees = numEmployees

    def efectivity(self):
        return self.capacity/self.numEmployees

hotel1 = Hotel("Fru Haugans Hotel", "Mosjøen", 300, 100)

print(hotel1.capacity)

print(hotel1.efectivity())