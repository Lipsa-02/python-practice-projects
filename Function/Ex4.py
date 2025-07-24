#Function for Cal Sum of Two Numbers
#ApproachEx4.py
#INPUT      : Input Taking in Function Body
#PROCESS    : Processing Done in Function Body
#RESULT     : Result Displayed Function Call
def sumop():
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    c=a+b
    return a,b,c
#main program
k,v,r=sumop() # Function Call with Multi Line assignment
print("Sum({},{})={}".format(k,v,r))#----Sum(8.0,9.0)=17.0
print("--*--"*45)
result=sumop()
print("Sum({},{})={}".format(result[0],result[1],result[2]))
#print("Sum({},{})={}".format(result[-3],result[-2],result[-1]))