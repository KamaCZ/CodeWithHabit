# creating a Circle class
class Circle():

    # creating an object attribute (common for all insstances of a Class)
    pi = 3.14

    # defining attributes of the Class instances
    def __init__(self, radius=1): # we can have default argument value
        self.radius = radius
        # attribute name can be assigned other arguments
        self.area = radius * radius * Circle.pi # it can be slef.pi as well, but it is better to use Circle.pi

    # defining methods
    def setRadius(self,new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * Circle.pi

    def get_circumference(self):
        # rounding in python
        result = self.radius * 2 * Circle.pi
        return round(result,2)

        

circle1 = Circle(2)
print(circle1.radius)
print(circle1.area)


circle1.setRadius(5)
print(circle1.radius)
print(circle1.area)
print(circle1.get_circumference())


