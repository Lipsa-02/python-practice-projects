#JSONFileToDictObject.py
#program to read or loading Json record from Json file into doct object
import json
try:
    with open("student.json","r") as fp:
        dictobj=json.load(fp)
        print("-"*50)
        print("content")
        print(dictobj)
        print("Type of dictobj=",type(dictobj))
        print("-"*50)
        for k,v in dictobj.items():
            print("\t{}--->{}".format(k,v))
        print("-"*50)
except FileNotFoundError:
    print("Json File does not Exist")

