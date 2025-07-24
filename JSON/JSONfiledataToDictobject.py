#JSONfiledataToDictobject.py
#program for loading file data into dict object
import json
with open("D:\\JSONFILE\\student.json","r") as fp:
    dobj=json.load(fp)
    print("content of dobj",dobj)
    print("type of dobj",type(dobj))
    print("-"*68)
    for k,v in dobj.items():
        print("\t{}---->{}".format(k,v))
        