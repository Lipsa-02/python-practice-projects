a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))
if a>b and a>c:
    print("{} is greater".format(a))
if b>a and b>c:
    print("{} is greater".format(b))
if c>a and c>b:
    print("{} is greater".format(c))
if a==b==c:
    print("{} , {} ,{} are equal".format(a,b,c))
print("program execution is completed")