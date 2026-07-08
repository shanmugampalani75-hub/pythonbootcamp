#OOP

#Inheritance
class Shape: #Parent class
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Circle(Shape): #child inherits its parent Shape
    def __init__(self, radius):
        super().__init__("Test")
        self.radius = radius

    def area(self): # override parent method
        return 3.14 * self.radius * self.radius


class Square(Shape):  #child inherits from Shape
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side

# both Circle and Square inherit 'name' attribute from Shape
circle = Circle(5)
square = Square(4)

# print(circle.name)
# print(square.name)
# print(circle.area())

#Polymorphism
def print_area(shape):
    print(f"{shape.name} area: {shape.area()}")

#same method call, different behaviors
print_area(circle)
print_area(square)

# or with a list
shapes = [Circle(3), Square(5), Circle(2)]
for shape in shapes:
    print_area(shape) #Same code, different results]