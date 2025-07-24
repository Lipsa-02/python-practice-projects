#program for Reading the Words from KBD and Dsiplay
nov=int(input("enter number of words u want to input:"))
if(nov<=0):
    print("{} is invalid input".format(nov))
else:
    lst=list()
    for i in range(1,nov+1):
        val=input("enter {} word:".format(i))
        lst.append(val)
    else:
        print("list of words")
        print(lst)