class Town:

    def __init__(self, name, population, area, district):

        self.name = name
        self.population = population
        self.area = area
        self.district = district



town1 = Town("Konice",2500,17000,"Prostšjov")

print(town1.population)

