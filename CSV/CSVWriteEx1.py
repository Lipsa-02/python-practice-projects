#CSVWriteEx1.py
#program for creating CSV File and writing the records to the CSV File
import csv #step-1
colnames=["ENO","NAME","SAL","DSG"]#step-2
records=[[10,"Rossum",7.8,"Author"],
        [20,"Travis",5.8,"Scientist"],
        [30,"Hunter",5.6,"Analyzer"],
        [40,"Shiva",0.0,"student"],
        [50,"Ritche",7.5,"Developer"]]  #step-3
with open("D:\\CSV_for_use\\employee.csv","a") as fp: #step-4
    csvwr=csv.writer(fp) #step-5 #here csvwr is an class object of <class,_csv.write>  #step-5
    csvwr.writerow(colnames)  #step-6
    csvwr.writerows(records)  #step-7
    print("CSV File Created---verify")

