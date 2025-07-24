#program for Reading the Values from KBD and Dsiplay
nov=int(input("enter number of value u want to enter:"))
if(nov<=0):
    print("{} is invalid input".format(nov))
else:
    lst=[]
    for i in range(1,nov+1):
        val=float(input("enter {} value".format(i)))
        lst.append(val)
    else:
        print("list of values")
        print(lst)