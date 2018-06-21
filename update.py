import csv
from pymongo import MongoClient
def updateDirection(path):
    client = MongoClient('localhost', 27017)
    db = client.zhilian_scrapy
    details = db.cleans
    with open(path,encoding='utf_8_sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] != "":
                print(row["id"])
                db.collection.update_one({"_id":row["id"]},{"$set":{"direction":row["direction"]}})
            pass
        print("finish")
    pass

updateDirection(r"C:\Users\admin\testhz\data\cleans1_2018-01-31_3.csv")