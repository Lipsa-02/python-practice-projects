#FileOpenex2.py
with open("Hyd.data","w") as fp:
    print("File opened in write mode successfully")
    print("file name=",fp.name)
    print("file mode=",fp.mode)
    print("is the file readable=",fp.readable())
    print("is the file writable=",fp.writable())
    print("is the file closed=",fp.closed)
print("is file closed out-off with open() as indentation=",fp.closed)