import math
#define the class
class Circle:

    #create the class variables

    #create the init fuction
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3 * (self.radius ** 2)

    def get_volume(self):
        pass

#create methods get_area, get_volume
cir1 = Circle(5)
print(cir1.get_area())
