#Function for Cal Sum of Two Numbers
#ApproachEx1.py
#INPUT      : Input Taking from Function Call
#PROCESS    : Processing Done in Function Body
#RESULT     : Result Given to Function Call
def sumop(k,v):
    r=k+v
    return r
#main program
a=float(input("enter first number:"))
b=float(input("enter second number :"))
c=sumop(a,b)  #function call
print("sum({},{})={}".format(a,b,c))
print("--*--"*50)
k=int(input("enter value:"))
v=int(input("enter value:"))
r=sumop(k,v)
print("sum of {},{}={}".format(k,v,r))