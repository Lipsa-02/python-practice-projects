#CSVDictReaderEx2.py
import csv
with open("D:\\CSV_for_use\\Product.csv") as fp:
    csvdr=csv.DictReader(fp)#here csvdr is an object of
    for record in csvdr:
        for k,v in record.items():
            print("{}---->{}".format(k,v))
        print("-"*50)