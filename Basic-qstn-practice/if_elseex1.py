#program for accepting Two Numerical values and Find Biggest or equal using if else statement
a=int(input("enter value for a:"))
b=int (input("Enter value for b:"))
if a>b:
   print("\t\t{} is greater than {}".format(a,b))
else:
    if b>a:
        print("\t\t{} is greater than {}".format(b,a))
    else:
        print("\t\t {} and {} both are equal".format(a,b))
        print("I'm from inner if else loop")
print("I'm from outer if else loop")