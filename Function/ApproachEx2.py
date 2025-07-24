#function for cal sum of two Numbers
#ApproachEx2.py
def sumop(a,b):#here a,b are called formal parameters
    print("i am from sumop() defination")
    c=a+b  #here c is called local variable
    return c

#main program
z=sumop(13,22)#function call
print("sum=",z)
print("*"*40)
c=sumop(1999,111)#function call
print("sum=",c)
print("*"*40)
c=sumop(-100,-200)
print("sum=",c)