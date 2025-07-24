#program for adding two numbers by using function
def sumop(a,b):
    c=a+b
    return c

#main program
x=float(input("enter x:"))
y=float(input("enter y:"))
res=sumop(x,y)
print("sum {},{}={}".format(x,y,res))
