#create the parent class
class Vehicle:
    def __init__(self,name,color):
        #your code here
        self.name = name
        self.color = color

    def max_speed(self):
        #your code here
        pass
class Car(Vehicle):
    def max_speed(self):
        #your code here
        print("max speed is 150")

class Bus(Vehicle):
    def max_speed(self):
        #your code here
        print("max speed is 250")
#creat instance of the three classes and call the max_speed() function on them

car1 = Vehicle("Tesla", 'black')
car2 = Car("Toyota", 'red')
car3 = Bus("School Bus", 'Yellow')

car1.max_speed()
car2.max_speed()
car3.max_speed()
