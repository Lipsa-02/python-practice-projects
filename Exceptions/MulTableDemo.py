#MulTableDemo.py
from Exceptions.MulExcept import InvalidNumberError,ZeroError
from Exceptions.MulTable import table
while(True):
    try:
        n=input ("enter a number for generating mul table:")
        table(n)
    except InvalidNumberError:
        print("{} is invalid Number-try again:".format(n))
    except ZeroError:
        print("Don't enter zero for Mul table:")
    except ValueError:
        print("Don't enter alnums,symbols and spaces and float values for Mul Table")
    except:
        print("oops something went wrong")
    else:
        break