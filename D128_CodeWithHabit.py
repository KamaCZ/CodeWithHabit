# Object oriented programming

# classes


class Country:


    earth_circumference = 40075
    earth_radius = 6371

    def __init__(self,flag_colors,population,capital,land_area, circumference):
        self.flag_colors = flag_colors
        self.population = population
        self.capital = capital
        self.land_area = land_area
        self.circumference = circumference

    def density(self):
        return int(self.population / self.land_area)

    def length_multiplyer(self):
        # how many times is Earth's circumference of the country's circumference
        return int(self.circumference / self.earth_circumference)


norway = Country(["red","blue","white"],5391369,"Oslo",385207, 25000)   
czechia = Country(["red","blue","white"],10707839,"Prague",78866, 2326)  
indonesia = Country(["red","white"],270203917,"Jakarta",1904569, None) 

print(norway.land_area)

print(norway.density())
print(czechia.density())
print(indonesia.density())
print(czechia.earth_radius)
print(norway.circumference)
print(indonesia.circumference)
print(indonesia.length_multiplyer())
print(norway.length_multiplyer())


# fixing the None value



