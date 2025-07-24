#dictobjectTojsonfile.py
#program for converting dict object data into json string format
import json
print("-"*59)
dictobj={"SID":100,"NAME":"swarna","Marks":87}
print("content of dictobj",dictobj)
print("type of dictobj:",type(dictobj))
print("-"*59)
#saving the object data to the json file
with open("D:\\JSONFILE\\student.json","w") as fp:
    json.dump(dictobj,fp)
    print("dict object data saved in json file----verify")