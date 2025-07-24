#Function for Cal Sum of Two Numbers
#INPUT      : Input Taking in Function Body
#PROCESS    : Processing Done in Function Body
#RESULT     : Result Displayed Function Body

def sumop():
    #taking input in function value
    a=int(input("enter value1:"))
    b=int(input("enter value2:"))
    #processing
    c=a+b
    #display result in function body
    print("sum of {},{} is={}".format(a,b,c))
#main program
sumop()