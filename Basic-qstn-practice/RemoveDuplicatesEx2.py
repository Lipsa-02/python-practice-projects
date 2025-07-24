#Program for Eliminating Duplicates from Line of Text without using set()
n=input("enter line of text:")
lst=list()
for ch in n:
    if ch not in lst:
        lst.append(ch)
else:
    print("given line =",n)
    print("unique value=","".join(lst))