#CSVDynamicWriteEx1.py
#program for creating dynamic csv file-----(List in List)
#by creating header names and list data (Records)
import csv
def dynamiccsvfile():
    try:
        noc=int(input("enter how many number of names you want :"))
        if(noc<=0):
            print("/t{} invalid number of header names".format(noc))
        else:
            hnames=[]
            for i in range(1,noc+1):
                colnames=input("enter {} colnames:".format(i))
                hnames.append(colnames)
            else:
                try:
                    nor=int(input("enter the number of records you want:"))
                    if(nor<=0):
                        print("{} invalid number of header names".format(noc))
                    else:
                        records=[]
                        for i in range(1,nor+1):
                            print("-"*50)
                            print("enter {} record details".format(i))
                            print("-"*50)
                            record=[]
                            for j in range(len(hnames)):
                                values=input("enter value for'{}':".format(hnames[j]))
                                record.append(values)
                            else:
                                records.append(record)
                        else:
                            #print (records)
                            #choose the csv file amd open in write mode
                            while(True):
                                csvfilename=input("enter csv file name with an extension of .csv:")
                                if(csvfilename.endswith(".csv")):
                                    with open("D:\\CSV_for_use\\"+csvfilename,"a") as fp:
                                        csvwr=csv.writer(fp)
                                        csvwr.writerow(hnames)
                                        csvwr.writerows(records)
                                        print("CSV file created sucessfully....verify")
                                        break
                                else:
                                    print("invalid file name...try again")
                except ValueError:
                    print("/t donot enter alnums,strs and symbols for number of records")
    except ValueError:
        print("don't enter alnums,strs,symbols for number of records")
#main program
dynamiccsvfile()