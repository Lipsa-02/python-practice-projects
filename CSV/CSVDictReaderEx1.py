#CSVDictReaderEx1.py
#program for reading the data from CSV file in the form of dict by using DictReader
import csv
with open("D:\\CSV_for_use\\stdfile.csv") as fp:
    csvdr=csv.DictReader(fp)#here csvdr is an object of
    for record in csvdr:
        for k,v in record.items():
            print("{}---->{}".format(k,v))
        print("-"*50)