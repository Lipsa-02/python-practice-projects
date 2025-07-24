#program for demonstrating how to write data to file
#FilewriteEx2.py
sno=int(input("enter student number:"))
sname=input("enter student name:")
marks=input("enter student marks:")#here sno,sname,marks are objects resides in main memory
#save the data into the file
with open("student","w") as fp:
    fp.write(str(sno)+ "\t")  #as only str type data can be added through write()
    fp.write(sname +"\t")
    fp.write(str(marks)+"\n")  #as only str type data can be added through write()
    print("Data written to the file:")