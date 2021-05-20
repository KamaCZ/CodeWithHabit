import country

class Continent(country.Country):

    def __init__(self,name,population,contitnent_area):
        self.name = name
        self.population = population
        self.continent_area = contitnent_area


    def density(self):
        return self.population / self.continent_area

    
