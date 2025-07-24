#programfor opening the file
#test1.py
try:
    fp=open("Hyd.data","r")
    print("file opened in read mode")
except FileNotFoundError:
    print("File does not exist")
else:
    print("Type of fp=",type(fp))
    print("File opened")