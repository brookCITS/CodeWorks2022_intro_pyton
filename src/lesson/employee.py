class employee:
    num_employee=0
    raise_amount=1.00
    def __init__(self, name, sal):
        self.name=name
        self.sal=sal
        self.email=name + '@company.com'
        employee.num_employee+=1
        
    def apply_raise (self):
        self.sal=int(self.sal* raise_amount)

class developer(employee):
    raise_amount = 1.10
