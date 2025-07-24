#MulTable.py
from Exceptions.MulExcept import InvalidNumberError,ZeroError
def table(n):
    num=int(n)
    if(num<0):
        raise InvalidNumberError
    elif(num==0):
        raise ZeroError
    else:
        print("--*--"*50)
        print("Mul table for :{}".format(num))
        for i in range(1,11):
            print("\t{} X {}={}".format(num,i,num*i))
        print("--*--"*50)

