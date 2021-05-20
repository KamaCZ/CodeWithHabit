# Object oriented programming

# classes


class Country:

    def __init__(self,flag_colors,population,capital,land_area):
        self.flag_colors = flag_colors
        self.population = population
        self.capital = capital
        self.land_area = land_area


norway = Country(["red","blue","white"],5391369,"Oslo",385207)      

print(norway.land_area)


    