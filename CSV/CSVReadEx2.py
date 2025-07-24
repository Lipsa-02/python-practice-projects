#CSVReadEx2.py
#program to read data from the employee csv file
import csv
with open("D:\\CSV_for_use\\employee.csv") as fp:
    csvr=csv.reader(fp)
    print("-"*50)
    for rec in csvr:
        for v in rec :
            print("{}".format(v),end="\t")
        print()
    print("-"*50)