#program for finding of line,words and characters from any file
#FileCountIntforEx.py
try:
    filename=input("enter any file name:")
    nl=0
    nw=0
    nc=0
    with open(filename) as fp:
        filedata=fp.readlines()
        for line in filedata:
            nl=nl+1
            nw=nw+len(line.split())
            nc=nc+len(line)
        else:
            print("-"*50)
            print("number of lines={}".format(nl))
            print("number of words={}".format(nw))
            print("number of characters={}".format(nc))#"\n" also counted
            print("-" * 50)
        #print("Number of lines:",len(filedata))
        #print(filedata)

except FileNotFoundError:
    print("file does not exist")