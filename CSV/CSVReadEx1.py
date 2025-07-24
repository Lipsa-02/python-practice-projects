#CSVReadEx1.py
#program for reading the data from csv files concept
import csv
with open("D:\\CSV_for_use\\stdfile.csv") as fp:
    csvr=csv.reader(fp)#csvr is an object of <class,_csv.reader>
    print("="*60)
    for rec in csvr:
        for val in rec:
            print("{}".format(val),end="\t")
        print()
    print("="*60)