#FileOpenex4.py
with open("Stud1.data","x") as fp:
    print("-"*50)
    print("File opened in eXclusively in write mode successfully")
    print("file name=",fp.name)
    print("file mode=",fp.mode)
    print("is the file readable=",fp.readable())
    print("is the file writable=",fp.writable())
    print("is the file closed=",fp.closed)
    print("-" * 50)
print("is file closed out-off with open() as indentation=",fp.closed)