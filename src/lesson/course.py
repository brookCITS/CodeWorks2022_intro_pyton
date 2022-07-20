#define the class
class Course:

    #define the class variables

    #define the init method
    def __init__(self, id, name, year, sems, p ):
        self.id = id
        self.name = name
        self.year = year
        self.semester = sems
        self.professor = p

    #define other methods
    def add_professor(self, p):
        self.professor  = p

    def get_course_name(self):
        return self.name

#use the class
english = Course('ENGL101', 'Rehtorical Anlys', '2022', 'summer', 'daba')
print(english.get_course_name())
print(english.name)
