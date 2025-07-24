#program for calculating (a+b)**2
a=float(input("Enter value for a:"))
b=float(input("Enter value for b:"))
val=a**2+b**2+2*a*b
print("(a+b)^2({},{})={}".format(a,b,val))
print("="*50)
a=float(input("Enter value for a:"))
b=float(input("Enter value for b:"))
val=(a+b)*(a+b)
print("(a+b)^2({},{})={}".format(a,b,val))
