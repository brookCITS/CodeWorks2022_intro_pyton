class Animal:
    def __init__(self,name):
        self.name=name

    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print('Woof!')

class Cat(Animal):
    def talk(self):
        print('MEOW!')

c= Cat('kitty')
c.talk()
d=Dog('Doggy')
d.talk()
