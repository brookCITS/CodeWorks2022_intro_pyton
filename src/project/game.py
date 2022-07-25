class Characters:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        pass

class Hero(Characters):
    def move(self, speed):
        self.position = self.position + speed
        print("Moved "+self.name+" to "+str(self.position))

class Villain(Characters):
    def move(self, speed):
        self.position = self.position - speed
        print("Moved "+self.name+" to "+str(self.position))

hero = Hero("Joe")
villain = Villain("Jack")
villain.position = 10

while hero.position is not villain.position:
    villain.move(1)
    hero.move(0)
    print("\n")
