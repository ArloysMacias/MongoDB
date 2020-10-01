import pymongo
import dns # required for connecting with SRV


DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

client = pymongo.MongoClient("mongodb+srv://root:6posr3sb@myfirstcluster.2aykg.mongodb.net/myTestDB?retryWrites=true&w=majority")
db = client.test

conn = db

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)