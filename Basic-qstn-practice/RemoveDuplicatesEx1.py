#Program for Eliminating Duplicates from Line of Text by using set()
n=input("enter the line /word:")
s=set(n)
print("Given Line={}".format(n))
print("Unique values in line:","".join(s))