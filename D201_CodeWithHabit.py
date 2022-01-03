class Employee:

    def __init__(self, name, surname, salary, age):

        self.name = name
        self.surname = surname
        self.salary = salary
        self.age = age


employee1 = Employee("Kamil","Klemsa",180,29)


print(employee1.surname)