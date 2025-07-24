#CSVWriteEx2.py
import csv
record=[60,"KV",0.0,"Trainer"]
with open("D:\\CSV_for_use\\employee.csv","a") as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(record)
    print("record added to existing csv file-----verify")
