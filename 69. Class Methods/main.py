class Employee:
    company = "APPLE"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod ## FOR CHANGING THE WHOLE CLASS COMPANY
    def changeCompany(cls, newCompany):
        cls.company = newCompany
    
e1 = Employee()
e1.name = "Soumodip"
e1.show()
e1.changeCompany("TESLA")
e1.show()
print(Employee.company)