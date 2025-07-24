#program to accept 2 numeric value and find the biggest among them and check for equality by using simple if statement.
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
if a>b:
    print("{} is greater than {}".format(a,b))
if a<b :
    print("{}is greater than{}".format(b,a))
if a==b:
    print("{} and {} both are equal".format(a,b))
print("program execution is over")