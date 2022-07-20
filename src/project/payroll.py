from lesson.employee import Employee, Developer, Lead

#---------------------------------------------------------------
# your code here
class Payroll:

    #init function



    #add_employee()



    #get_payroll()




# ---------------------------------------------------------------



payroll = Payroll("Code Works")

payroll.add_employee(Employee('John', 20))
payroll.add_employee(Developer('Jane', 22))
payroll.add_employee(Lead('Molly', 25))

payroll.get_payroll()
