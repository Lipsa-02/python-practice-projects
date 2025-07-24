#icici.py<----- file name and acts as module name
bname="ICICI"
addr="BBSR-ODI"#bname,addr are global variable
def simpleint():#function Definition
    p=float(input("enter principle value:"))
    t=float(input("enter time:"))
    r=float(input("enter ratio:"))
    si=(p*t*r)/100
    totamt=si+p
    print("Simple interest is:{}".format(si))
    print("total amount is:{}".format(totamt))

