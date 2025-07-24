#program for copying the content of one file(source file)into another(destination file)
#FilecopyEx1.py
try:
    srcfile=input("enter source file:")
    with open(srcfile,"r") as rp:    #"rp" stands for read pointer
        dstfile=input("enter destination file:")
        with open(dstfile,"a") as wp:
            #read the data from source file
            srcfiledata=rp.read()
            #write the src file data to destination file
            wp.write(srcfiledata) #wp:- write pointer
            print("source file content copied into dest. file")
except FileNotFoundError:
    print("file does not exist")