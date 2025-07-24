#program for reading the data from keyboard and write to the file
#FilewriteEx4.py
print("Enter the information about python : ")
with open("new.data","a") as fp:
    while(True):
        Kbdata=input()
        if(Kbdata!="@"):
            fp.write(Kbdata+"\n")
        else:
            print("Data written to the file----verify")
            break