#program to find (a**m/a**n)
a=float(input("enter value for a:"))
m=float(input("enter value for m:"))
n=float(input("enter value for n:"))
v=(a**m)/(a**n)
print("\t\tresult is ({},{},{})={}".format(a,m,n,v))
print("="*50)
a=float(input("enter value for a:"))
m=float(input("enter value for m:"))
n=float(input("enter value for n:"))
v=a**(m-n)
print("\t\tresult is ({},{},{})={}".format(a,m,n,v))