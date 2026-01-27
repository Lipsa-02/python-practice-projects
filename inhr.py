from numpy.testing.print_coercion_tables import print_new_cast_table


class univ:
    def getun(self):
        self.unname= input("enter the university name:")
        self.unloc=input("enter university location:")
    def displayun(self):
        print("University Name:",self.unname)
        print("University Location:",self.unloc)
class clg(univ):
    def getclg(self):
        self.clgname=input("enter collage name")
        self.clgloc=input("enter collage location:")
    def displayclg(self):
        print("Collage Name:",self.clgname)
        print("Collage Location:",self.clgloc)
class student(clg):
    def getstd(self):
        self.stdname=input("enter student name:")
        self.stdnum=int(input("enter student number:"))
        self.stdcrs=input("enter student course:")
    def displaystd(self):
        print("Student Name:",self.stdname)
        print("Student Number:",self.stdnum)
        print("Student Course:",self.stdcrs)
#main program
s=student()
s.getun()
s.getclg()
s.getstd()
s.displayun()
s.displayclg()
s.displaystd()