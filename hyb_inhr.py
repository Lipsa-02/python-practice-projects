class person():
    def __init__(self,name):
        self.name=name
class Employee(person):
    def role(self):
        print(self.name,"is an employee")
class project():
    def __init__(self,prj_name):
        self.prj_name=prj_name
class TeamLead(Employee,project):
    def __init__(self,name,prj_name):
        Employee.__init__(self,name)
        project.__init__(self,prj_name)
    def details(self):
        print(self.name,"Lead project:",self.prj_name)
#main program
tl=TeamLead("Sivani","AI Development")
tl.role()
tl.details()