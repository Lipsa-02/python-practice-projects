try:
    with open("Hyd.data","r") as fp:
        fdata=fp.readlines()
        for val in fdata:
            print(val,end=" ")
except FileNotFoundError:
    print("File does not exist")