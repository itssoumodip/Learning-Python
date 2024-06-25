
# public access specifier
class Employe:
    def __init__(self):
        self.name = "Harry"


a = Employe()
print(a.name)

# private acess modifier
class Employe2:
    def __init__(self):
        self.__name = "Harry"

# a2 = Employe()
# print(a.__name)   ## we cannot accessed directly
a2 = Employe2()
print(a2._Employe2__name) ## can be accesed indirectly(name mangling)

# (name mangling) - print(a.__dir__())
print(a.__dir__())

#protected access modifier
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())

