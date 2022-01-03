class CodingLanguage:

    def __init__(self, name, type, totalCoders, popularityRank):

        self.name = name
        self.type = type
        self.totalCoders = totalCoders
        self.populartiyRank = popularityRank


language1 = CodingLanguage("Python", "OOP",10000000, 1)


print(language1.type)
