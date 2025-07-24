#program for accepting a Number and decide whether the given Number is prime or not
n=int(input("enter the number:"))
if(n<=0):
    print("invalid input")
else:
    res="prime"
    for i in range(2,n):
        if(n%i==0):
            res="Not a prime number"
            break
    print("{} is {}".format(n,res))