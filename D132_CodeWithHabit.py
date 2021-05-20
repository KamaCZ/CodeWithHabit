from country import Country
import country

australia = Country("Australia",["blue","white","red"],25794600,"Canberra",7692024,25740)
norway = Country("Norway",["red","blue","white"],5391369,"Oslo",385207, 25000)   
czechia = Country("Czechia",["red","blue","white"],10707839,"Prague",78866, 2326)  
indonesia = Country("Indonesia",["red","white"],270203917,"Jakarta",1904569, None) 

# inheritance

class Continent(country.Country):

    def __init__(self,name,population):
        self.name = name
        self.population = population


europe = Continent("europe",746400000)

print(europe.population)
print(europe.earth_radius)

