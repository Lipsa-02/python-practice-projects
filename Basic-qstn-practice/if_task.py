#given an integer n,perform the following task
#i.


n=int(input("enter value of n:"))
if n%2!=0:
    print("Weird")
if n%2==0 and n>=2 and n<=5:
    print("not Weird")
if n%2==0 and 6<=n<=20:
    print("Weird")
if n%2==0 and n>20:
    print("not Weird")