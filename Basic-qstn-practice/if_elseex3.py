#Proghram for accepting a Digit and Display It's Name
N=int(input("enter any digit:"))
if N==0:
    print("{} is zero".format(N))
else:
    if N==1:
        print("{} is one".format(N))
    else:
        if N==2:
            print("{} is two".format(N))
        else:
            if N==3:
                print("{} is three".format(N))
            else:
                if N==4:
                    print("{} is four".format(N))
                else:
                    if N==5:
                        print("{} is five".format(N))
                    else:
                        if N==6:
                            print("{} is six".format(N))
                        else:
                            if N==8:
                                print("{} is eight".format(N))
                            else:
                                if N==9:
                                    print("{} is nine".format(N))
                                else:
                                    if N>9:
                                        print("{} is+ve number".format(N))
                                    else:
                                        if N<0 and N in range(-1,-10,-1):
                                            print("{} is-ve number".format((N)))
                                        else:
                                            print("{} is -ve number".format(N))