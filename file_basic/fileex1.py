#Program Opening the File in read mode
#fileex1.py
try:
    fp=open("aop.py","r")
except FileNotFoundError:
    print("file does not exist")
else:
    print("type of fp=",type(fp))
    print("file opened in read+ mode")
    print("is file opened in read mode successfully")
finally:
    print("----finally----")
    try:
        print("is file closed before close()=",fp.closed)
        fp.close()
        print("Is File Closed after close()=", fp.closed)
    except NameError:
        print("file not opened yet,no need to close")