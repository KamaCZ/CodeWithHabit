class Person:

    def __init__(self, name, age, ethnicity, rate):
        self.name = name
        self.age = age
        self.ethnicity = ethnicity
        self.rate = rate


Peter = Person(30, "Peter", "czech", 3)

print(Peter.age)