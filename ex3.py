from pymongo import MongoClient
from matplotlib import pyplot
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_database()

collection = db["customers"]

customers = collection.find()

events = 0
ads = 0
wom = 0
for i in customers:
    if i["ref"] == "events":
        events += 1
    elif i["ref"] == "ads":
        ads += 1
    elif i["ref"] == "wom":
        wom += 1
print("events customers: " , events)
print("advertisements customer: ", ads)
print("word of mouth customer: ", wom)

#*******************************************************

ref_count = [events, ads, wom]
ref_labels= ['events', 'ads', 'wom']
pyplot.pie(ref_count, labels=ref_labels, autopct='%1.1f%%')
pyplot.axis("equal")
pyplot.show()

