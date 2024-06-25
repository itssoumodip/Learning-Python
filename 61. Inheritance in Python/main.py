class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails (self):
        print(f"The name of Employee : {self.id} is {self.name}")

class Programmer(Employee):
    def ShowLanguage(self):
        print("The default Language is Python")
e = Employee("Rohan Das", 420)
e.showdetails()
e2 = Programmer("Soumodip", 450)
e2.showdetails()
e2.ShowLanguage()