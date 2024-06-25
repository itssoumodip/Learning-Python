class person:
    name = "Soumodip"
    occupation = "Software Developer"
    networth = 10
    def info (self):
        print(f"{self.name} is a {self.occupation}")
        

a = person()
a.name = "Shubham"
a.occupation = "Accountant"
# print(a.name, a.occupation) 
b = person()
b.name = "Kriticka"
b.occupation = "HR"
c = person()
a.info()
b.info()
c.info()

