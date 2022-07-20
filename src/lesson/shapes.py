import math
class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class circle(Shape):
    def __init__(self, r):
        super().__init__('Circle')
        self.radius = r

    def area(self):
        self.area = 3 * (self.radius ** 2.0)
        return self.area


cir = circle(5)
print(cir.area())
