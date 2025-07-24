#FileAttributeex1.py
try:
    fp=open("Hyd.data","r")
except FileNotFoundError:
    print("File does not exist")
else:
    print("FIle opened in read mode successfully")
    print("File name:",fp.name)
    print("file mode:",fp.mode)
    print("Is file Readable=",fp.readable())
    print("Is file writable=",fp.writable())
    print("Is file closed =",fp.closed)
finally:
    print("I am from Finally Block ")
    fp.close()
    print("Is file closed=",fp.closed)