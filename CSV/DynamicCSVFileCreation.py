#DynamicCSVFileCreation.py
import csv
noc=int(input("enter no. of values you want to enter in csv file:"))
if(noc<=0):
    print("invalid input----try again")
else:
    cname=[]
    for i in range(1,noc+1):
        colname=input("Enter {} col name:".format(i))
        cname.append(colname)
    else:
        print(cname)
        nor=int(input("enter how many records you want to enter:"))
        if (nor<=0):
            print("invalid no of records---try again")
        else:
            records=[]#for adding multiple records---outer list
            for nr in range(1,nor+1):
                print("enter {} record data:".format(nr))
                record=[]#for adding single record----inner list
                for cn in range(0,len(cname)):
                    val=input("enter {} value:".format(cname[cn]))
                    record.append(val)
                else:
                    records.append(record)
            else:
                #choose the csv file name and save data
                filename=input("enter a file name with extension of .csv:")
                if(not filename.endswith(".csv")):
                    print("try to give extension.csv")
                else:
                    with open("D:\\CSV_for_use\\"+filename,"a")as fp:
                        csvwr=csv.writer(fp)
                        csvwr.writerow(cname)
                        csvwr.writerows(records)
                        print("CSV file created dynamically----verify")






