class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def role(self):
        print(self.name,"work as an employee")
class Intern(Person):
    def role(self):
        print(self.name,"is an intern")
#main program
emp= Employee("Dany")
emp.role()
intr= Intern("Tris")
intr.role()
