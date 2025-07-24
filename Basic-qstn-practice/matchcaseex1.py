import sys

print("*"*60)
print("\t\tArithmatic operation")
print("*"*60)
print("\t\t1.Addition")
print("\t\t2.Subtraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Floor Division")
print("\t\t6.Modulo Division")
print("\t\t7.Exponent")
print("\t\t8.Exit")
print("*"*60)
ch=int(input("Enter your choice:"))
match(ch):
    case 1:
        a=float(input("Enter First Value for addition:"))
        b=float(input("Enter Second Value for addition:"))
        print("\t\tSum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter two Values for Subtraction")
        a,b=float(input()),float(input())
        print("\t\tSub({},{})={}".format(a, b, a - b))
    case 3:
        print("enter two value for Multiplication:")
        a,b=float(input()),float(input())
        print("\t\tMul({},{})={}".format(a,b,a*b))
    case 4:
        a=float(input("Enter value fpt div:"))
        b=float(input("Enter value for div:"))
        print("\t\tDiv({},{})={}".format(a,b,a/b))
    case 5:
         a=float(input("enter value for floor div:"))
         b=float(input("enter value for floor div:"))
         print("\t\tFloor div({},{})={]".format(a,b,a//b))
    case 6:
            a=float(input("enter value for mod div:"))
            b=float(input("enter value for mod div:"))
            print("\t\tmod div({},{})={}".format(a,b,a%b))
    case 7:
            a=float(input("enter value for base:"))
            b=float(input("enter value for power:"))
            print("\t\tpow({},{})={}".format(a,b,a ** b))
    case 8:
            print("thanks for using program")
            sys.exit()
    case _:
            print("Your selection of operation is WRONG-- try again")
print("match case program completed")

