#program for displaying the content of file
#FileDisplayContent.py
try:
    filename=input("enter the file Name to view it's content:")
    with open(filename,"r") as fp:
        filedata=fp.read()
        print("-"*50)
        print("content of file")
        print("-" * 50)
        print(filedata)
        print("-"*50)
except FileNotFoundError:
    print("File does not exist")