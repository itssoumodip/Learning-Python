class Employee:
    company_name = "ABC Limited"
    noOfEmployess = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployess +=1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the Raise amout in {self.noOfEmployess} sized {self.company_name} is {self.raise_amount}")

emp1 = Employee("Harry")
emp1.raise_amount = 0.03
emp1.company_name = "AMR school"
Employee.company_name = "Goggle"
print(Employee.company_name)
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.company_name = "Nestle"
emp2.showDetails()
# Employee.showDetails(emp1)