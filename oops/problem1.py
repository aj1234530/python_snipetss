class Employee:
    company_name = "Dragon"
    total_employee = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total_employee += 1
    def get_name(self):
        print(f"{self.first_name} {self.last_name}")
    
e1 = Employee("john","doe")
e2 = Employee("abhi","jay")

print(e1.get_name(),e1.first_name,e1.total_employee)
print(e1.first_name,e1.last_name) #works
print(Employee.total_employee) # as it is class variable
print(e2.get_name(),e2.total_employee)

print(e2.first_name,e2.last_name) #works
