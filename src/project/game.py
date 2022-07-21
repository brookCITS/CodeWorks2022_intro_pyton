#define the class
class Character:
    #define the class variables
    characters = []

    #define the the init function
    def __init__(self, name):
        #your code here
        self.name = name
        self.level = 0
        self.lives = 3
        self.position = 0
        Character.characters.append(self)
    #add the methods
    def move(self, speed):
        #your code here
        self.position = self.position + speed
        print("moved to: "+ str(self.position))

    def level_up(self):
        #your code here
        self.level = self.level + 1
        print("New Level: "+str(self.level))
    def kill(self):
        #your code here
        self.lives = self.lives - 1
        self.mylives()

    def bonus(self):
        #your code here
        self.lives = self.lives + 1
        self.mylives()

    def mylives(self):
        print("You have "+ str(self.lives)+" lives left")

#create 4 instance of this class and test all the methods
char1 = Character("Joe")
char1.move(3)
char1.level_up()
char1.kill()
char1.kill()
char1.bonus()
