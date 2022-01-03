class Investor:

    def __init__(self, name, nationality, countries):
        self.name = name
        self.nationality = nationality
        self.countries = countries

    def countriesNumber(self):
        return len(self.countries)


investor1 = Investor("Kama","Czech",("Norway","Poland","Czechia","Austria","Spain"))


print(investor1.countries)

print(investor1.countriesNumber())


