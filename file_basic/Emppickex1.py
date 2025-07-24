#progrsm for reading the employee details from keyboard and save them to secondary memory
#EmppickEx.py
import pickle
def saveemprecord():
    with open("emp.pick","ab") as fp:
        while(True):
            #read the emp data from keyboard
            empno=int(input("enter employee number:"))
            empname =input("enter employee name:")
            sal=float(input("enetr employee salary:"))
            dsg=input("enter employee designation:")
            print("-"*50)
            #add employee values to iterable object
            lst=[]
            lst.append(empno)
            lst.append(empname)
            lst.append(sal)
            lst.append(dsg)
            #save the object data to the file
            pickle.dump(lst,fp)
            print("employee record saved in a file")
            print("-"*56)
            ch=input("Do you want to insert another record(yes/no):")
            if(ch.lower()=="no"):
                print("thanks for using the program")
                break
#main program
saveemprecord()  #function call