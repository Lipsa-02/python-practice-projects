#program for accepting Three Numerical values and find Max and Check for Equality
#TernaryOpEx5.py
#Accepting Three values from KBD
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
#Code for Finding Max and equaliy
res=a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All Values are equal"
print("Max({},{},{})={}".format(a,b,c,res))1