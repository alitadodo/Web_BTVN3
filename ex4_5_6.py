from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_database()
collection = db["river"]
# print(collection)

all_river_africa = collection.find({"continent": "Africa"})
for i in all_river_africa:
    print(i)

#***********************************************************

america_small = collection.find({"continent": "S. America"})
for j in america_small:
    if j["length"] < 1000:
        print(j)