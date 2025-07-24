#CSVDictWriteEx1.py
#creating csv file with dict data
import csv
hname=["PID","PNAME","PRICE"]
records=[{"PID":100,"PNAME":"nestle","PRICE":100.00},
        {"PID":200,"PNAME":"Kit-Kat","PRICE":40.00},
        {"PID":300,"PNAME":"Kinderjoy","PRICE":50.00},
        {"PID":400,"PNAME":"Dairy-milk","PRICE":20.00}]
with open("D:\\CSV_for_use\\Product.csv","a") as fp:
    csvwdr=csv.DictWriter(fp,fieldnames=hname)
    csvwdr.writeheader()
    csvwdr.writerows(records)
    print("CSV File created and vereify")
