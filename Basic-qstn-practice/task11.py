#program for finding area of triangle
#formula-1
br=float(input("enter value for breadth:"))
ht=float(input("enter value for height:"))
area=1/2*br*ht
print("area of triangle is({},{})={}".format(br,ht,area))
print("*"*50)
#formula-2
a=float(input("enter value for a:"))
b=float(input("enter value for b:"))
c=float(input("enter value for c:"))
s=(a+b+c)/2
A=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of the triangle is({},{},{},{})={}".format(a,b,c,s,A))
print("="*50)