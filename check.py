import csv
from pymongo import MongoClient
import os
dicJSDev = ["INT","BD","JS","VR","REQ","PRD","DESIGN","MT","SELL","IOS","DOTNET","ANDROID","TEST",
"R","C","JAVA","PHP","CPLUS","PYTHON","HTML","RUBY","ABAP","PERL","GO","SCALA","PB","ORA","SQL","MYSQL",
"MONGODB","REDIS","NONE"
]

def check(path):
    with open(path,encoding='utf_8_sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not (row["direction"] in dicJSDev):
                print(reader.line_num,row["direction"])
                pass
            pass
    pass

check(r"C:\Users\admin\testhz\data\cleans1_2018-01-31_5.csv")