# define the class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def getCar(self):
        info = "make :"+self.make+" | model: "+self.model
        return info

    def __str__(self):
        return "make :"+self.make+" | model: "+self.model

#define the class variables

#define the the init function

#add the methods




#create instance of the class and print them out
toyota = Car('Toyota', 'Corola')
print(toyota)
