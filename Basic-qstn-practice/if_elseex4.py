#Program for accepting a value and Decide weather It is even or odd for +ve Numbers
n=int(input("enter value for n:"))
if n>0 and n%2==0:
    print("{} is even".format(n))
else:
    if n>0 and n%2!=0:
        print("{} is odd".format(n))
    else:
        print("-ve number")