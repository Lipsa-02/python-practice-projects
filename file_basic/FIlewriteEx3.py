#program for demonstrating how to write data to file
#FilewriteEx3.py
x={10:"python",20:"Rossum",30:"van",40:"Guido"} #here x is called iterable object
fp=open("student1","a")
fp.writelines(str(x)+"\n")
print("iterable object written to the file")