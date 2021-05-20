from country import Country

australia = Country("Australia",["blue","white","red"],25794600,"Canberra",7692024,25740)
norway = Country("Norway",["red","blue","white"],5391369,"Oslo",385207, 25000)   
czechia = Country("Czechia",["red","blue","white"],10707839,"Prague",78866, 2326)  
indonesia = Country("Indonesia",["red","white"],270203917,"Jakarta",1904569, None) 

print(australia)

print(australia.density())
print(norway.density())
print(czechia.density())
print(indonesia.density())

