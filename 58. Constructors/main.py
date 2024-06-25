class Person:
    # name = "Harry"
    # occ = "Developer"

    def __init__(self, n, o):
        print("Hey I am a Person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Harry", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# # print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()

class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()

