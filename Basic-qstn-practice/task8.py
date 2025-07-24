#program for finding (a**m)**n
a=float(input("enter value for a:"))
m=float(input("enter value for m:"))
n=float(input("enter value for n:"))
v=((a**m)**n)
print("result is ({},{},{})={}".format(a,m,n,v))
print("="*50)
v=(a**(m*n))
print("result is ({},{},{})={}".format(a,m,n,v))