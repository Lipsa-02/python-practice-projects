#Function for cal sum of two number
#INPUT      : Input Taking in Function Call
#PROCESS    : Processing Done in Function Body
#RESULT     : Result Displayed Function Body
def sumop(k,v):
    r=k+v
    print("sum of ({} , {})={}".format(k,v,r))
#main program
k=float(input("enter k value :"))
v=float(input("enter v value:"))
sumop(k,v) #function call