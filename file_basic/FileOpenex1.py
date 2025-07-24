#FileOpenex1.py
#fp=open("Stud.data")
#print("File opened in read mode succesfully")
#to overcome this problem
try:
    fp=open("Stud.data")
    print("file opened succesfully")
except FileNotFoundError:
    print("file does not exist")
