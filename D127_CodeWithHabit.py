# Object oriented programming

# classes


class Country:


    earth_circumferance = 40075
    earth_radius = 6371

    def __init__(self,flag_colors,population,capital,land_area):
        self.flag_colors = flag_colors
        self.population = population
        self.capital = capital
        self.land_area = land_area

    def density(self):
        return int(self.population / self.land_area)


norway = Country(["red","blue","white"],5391369,"Oslo",385207)   
czechia = Country(["red","blue","white"],10707839,"Prague",78866)  
indonesia = Country(["red","white"],270203917,"Jakarta",1904569) 

print(norway.land_area)

print(norway.density())
print(czechia.density())
print(indonesia.density())
print(czechia.earth_radius)



    