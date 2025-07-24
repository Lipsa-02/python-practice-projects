print("*"*60)
print("\t\tTemperature Conversion Calculator")
print("*"*60)
print("\t\t1.F to C")
print("\t\t2.F to K")
print("\t\t3.C to F")
print("\t\t4.C to K")
print("\t\t5.K to F")
print("\t\t6.K to C")
print("\t\t7.Exit")
print("*"*60)
ch=int(input("Enter your choice:"))
match (ch):
    case 1:
        f=float(input("enter tem to convert into celsius:"))
        print("\t\tcelsius{}={}".format(f,(f-32)*5/9))
    case 2:
        f=float(input("enter tem ro convert to kelvin:"))
        print("\t\tkelvin {}={}".format(f,((f-32)*5/9)+273.15))
    case 3:
        c=float(input("enter tem to convert to fahrenheit:"))
        print("\t\tfahrenheit {}={}".format(c,(c*9/5)+32))
    case 4:
        c=float(input("enter tem to convert to kelvin:"))
        print("\t\tkelvin {}={}".format(c,c+273.15))
    case 5:
        k=float(input("enter tem to convert to fahrenheit:"))
        print("\t\tfahrenheit{}={]".format(k,(k-273)*9/5+32))
    case 6:
        k=float(input("enter tem to convert to celsius:"))
        print("\t\tcelsius {}={}".format(k,k-273.15))
    case 7:
        print("\t\t Thanks for using the code")
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("match case program completed")