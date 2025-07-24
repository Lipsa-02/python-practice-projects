#progrsm for reading from file where it contains employee records (emp.pick)
#Empunpickeex2.py
import pickle
def reademprecords():
    try:
        with open("emp.pick","rb")as fp:
            print("-" * 50)
            print("Employee details:")
            print("-"*50)
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("{}".format(val),end="\t\t\t\t")
                    print()
                except EOFError:
                    print("-"*50)
                    break
    except FileNotFoundError:
        print("file does not exist")

#main program
reademprecords()