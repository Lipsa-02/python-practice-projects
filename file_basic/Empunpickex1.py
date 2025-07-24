#program for reading the records from file where it contains employee records
#Empunpickex1.py
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
                    print(record,type(record))
                    record = pickle.load(fp)
                    print(record,type(record))
                except EOFError:
                    break
    except FileNotFoundError:
        print("file does not exist")

#main program
reademprecords()