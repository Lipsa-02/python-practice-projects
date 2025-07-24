#Program for Cal simple Interest and Total amount to apy
def simpleint():
    p=float(input("enter principle value:"))
    t=float(input("enter time:"))
    r=float(input("enter ratio:"))
    si=(p*t*r)/100
    ta=p+si
    print("--*--"*45)
    return p,t,r,si,ta
#main program
sint=simpleint()
print("\tResults of Simple Interest".upper())
print("*"*50)
print("\tPrinciple Amount:{}".format(sint[0]))
print("\tTime:{}".format(sint[1]))
print("\tRate of Interest:{}".format(sint[2]))
print("\tSimple Interest:{}".format(sint[3]))
print("\tTotal Amount to Pay:{}".format(sint[4]))
print("*"*50)

