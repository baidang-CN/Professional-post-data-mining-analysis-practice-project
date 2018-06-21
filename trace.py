import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
client = MongoClient('localhost', 27017)
db = client.zhilian_scrapy
details = db.cleans
date = "2018-01-31"
df = pd.DataFrame(list( details.find({"date": date})))
df.loc[(df['direction'] != "NONE")].direction.count()
df.groupby('direction')['_id'].count()