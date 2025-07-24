#program for Demonstrating Access the data from file randomly
#1.tell()------->gives present index of file pointer where it points
#2.seek()-------->makes the file pointer to reset at specified index of existing file
#randomAccessFile.py
try:
    with open("Hyd.data","rt") as fp:
        print("initially,fp points to:",fp.tell())  #0
        filedata=fp.read(6)
        print(filedata)
        print("-"*58)
        print("Now fp points to :",fp.tell())
        filedata = fp.read(6)
        print(filedata)
        print("-" * 58)
        print("Now fp points to :", fp.tell())
        filedata = fp.read(6)
        print(filedata)
        print("-" * 58)
        print("Now fp points to :", fp.tell())
        filedata = fp.read()
        print(filedata)
        print("-" * 58)
        print("Now fp points to :", fp.tell())
        #to reset the file pointer object,we use seek()
        fp.seek(0)
        print("-" * 58)
        print("Now fp points to :", fp.tell())
        filedata = fp.read()
        if(len(filedata)==0):
         print("File pointer reaches to end the file")
        print("-" * 58)
except FileNotFoundError:
    print("file does not exist")