#program to accept any two values and compute all arithmetic operator by using multiline assignment operator
#addition(+)
a,b=input("enter value for a:"),input("enter value for b:")
s=a+b
print("sum of a and b{},{}={}".format(a,b,s))
print("*"*50)
#substraction(-)
a,c=int(input("enter value of a:")),int(input("enter value of c:"))
sub=(a-c)
print("subtraction a and b{},{}={}".format(a,c,sub))
print("*"*50)
#multiplication(*)
a,b=int(input("enter value of a:")),int(input("enter value of b:"))
mul=a*b
print("multiplication of a and b{},{}={}".format(a,b,mul))
print("*"*50)
#division(/)
a,b=int(input("enter value of a:")),int(input("enter value of b:"))
div=a/b
print("division of a and b{},{}={}".format(a,b,div))
print("*"*50)
# fllordivision(a//b)
a,b=int(input("enetr value of a:")),int(input("enter value of b:"))
fdiv=a//b
print("flloraldivision of a and b {},{}={}".format(a,b,fdiv))
print("*"*50)
#modulous(%)
a,b=float(input("enter value of a:")),float(input("enter value of b:"))
mod=a%b
print("modulous of a and b{},{}={}".format(a,b,mod))
print("*"*50)
