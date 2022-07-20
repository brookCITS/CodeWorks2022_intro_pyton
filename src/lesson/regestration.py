class Regestration:

    def __init__(self):
        self.roster = []
        self.roster_max = 20

    def register(self, student):
        if len(self.roster) < self.roster_max:
            self.roster.append(student)
            print("Registerd" +student)
        else:
            print("Registration Error: course is full")
