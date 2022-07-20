#define the class
class Person:
    #class Variable
    name = "Person"
    people = []

    #define init function
    def __init__(self, name = None):
        # self.name is the instance variable
        self.name = name

    def change_name(self, newName):
        self.name = newName

#using the class
jim = Person("Jim")

print(jim.name)

jim.change_name("Jimmy")

print(jim.name)
