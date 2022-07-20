import math
class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        super().__init__('Circle')
        self.radius = r

    def area(self):
        self.area = 3 * (self.radius ** 2.0)
        return self.area

class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__('Rectangle')
        self.radius = r
        self.length = l
        self.width = w

    def area(self):
        self.area = self.length * self.width
        return self.area


cir = Circle(5)
print(cir.name)
print(cir.area())

rec = Rectangle(3,4)
print(rec.name)
print(rec.area())
