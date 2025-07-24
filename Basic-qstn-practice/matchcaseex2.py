print("*"*60)
print("\t\tArea of different figures")
print("*"*60)
print("\t\tR.Rectangle")
print("\t\tS.square")
print("\t\tC.Circle")
print("\t\tT.triangle")
print("\t\tE.Exit")
print("*"*60)
ch=input("Enter your choice:")
match (ch):
    case "R":
        l=float(input("enter length for area of triangle:"))
        w=float(input("enter width for area of triangle:"))
        print("\t\tRec({},{})={}".format(l,w,l*w))
    case "S":
        a=float(input("enter side of square:"))
        print("\t\tsqr({},{})={}".format(a,a,a*a))
    case "C":
        r=float(input("enter value for radius"))
        print("\t\tcircle({})={}".format(r,3.14*r*r))
    case "T":
        l=float(input("enter length for area of triangle:"))
        b=float(input("enter breadth for area of triangle:"))
        print("\t\ttrn({},{})={}".format(l,b,0.5*l*b))
    case "E":
        print("Thanks for using the code")
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("Match case program completed")


