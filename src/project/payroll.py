from lesson.employee import Employee, Developer, Lead

#---------------------------------------------------------------
# your code here
class Payroll:

    #init function
    def __init__(self, name):
        self.name = name
        self.empList = []

    def add_employee(self, employee):
        self.empList.append(employee)

    def get_payroll(self):
        for emp in self.empList:
            print(emp.name + " | " + str(emp.payment(40)))




# ---------------------------------------------------------------



payroll = Payroll("Code Works")

payroll.add_employee(Employee('John', 20))
payroll.add_employee(Developer('Jane', 22))
payroll.add_employee(Lead('Molly', 25))

payroll.get_payroll()
