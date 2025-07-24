#FileOpenex3.py
with open("Stud.data","a+") as fp:
    print("File opened in append mode successfully")
    print("file name=",fp.name)
    print("file mode=",fp.mode)
    print("is the file readable=",fp.readable())
    print("is the file writable=",fp.writable())
    print("is the file closed=",fp.closed)
print("is file closed out-off with open() as indentation=",fp.closed)