#program for accepting a Number and decide whether the given Number is prime or not
n=int(input("enter the number:"))
if(n<=0):
    print("invalid input")
else:
    res=True
    for i in range(2,n):
         if(n%i==0):
             res=False
             break
    res= "prime" if res else "not a prime number"
    print("{} is {}".format(n,res))