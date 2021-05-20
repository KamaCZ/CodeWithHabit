# Object oriented programming

# classes


class Country:


    earth_circumference = 40075
    earth_radius = 6371

    def __init__(self,name,flag_colors,population,capital,land_area, circumference):
        self.name = name
        self.flag_colors = flag_colors
        self.population = population
        self.capital = capital
        self.land_area = land_area
        self.circumference = circumference

    def density(self):
        return int(self.population / self.land_area)

    def length_multiplyer(self):
        # how many times is Earth's circumference of the country's circumference
        try:
            return (self.circumference / self.earth_circumference)
        except:
            print("non-applicable for this country")

    def __str__(self):
        return f"Country: {self.name} \nCapital: {self.capital}\nPopulation: {self.population}"


norway = Country("Norway",["red","blue","white"],5391369,"Oslo",385207, 25000)   
czechia = Country("Czechia",["red","blue","white"],10707839,"Prague",78866, 2326)  
indonesia = Country("Indonesia",["red","white"],270203917,"Jakarta",1904569, None) 

#print(norway.land_area)

"""
print(norway.density())
print(czechia.density())
print(indonesia.density())
print(czechia.earth_radius)
print(norway.circumference)

print(indonesia.circumference)
"""
#print(indonesia.length_multiplyer())
#print(norway.length_multiplyer())

if __name__ == "__main__":
    print(norway)



#print(norway)



