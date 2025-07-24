try:
    fp=open("Hyd.data","r")
    print("FIle opened in read mode successfully")
    print("File name:", fp.name)
    print("file mode:", fp.mode)
    print("Is file Readable=", fp.readable())
    print("Is file writable=", fp.writable())
    print("Is file closed =", fp.closed)
except FileNotFoundError:
    print("File does not exist")