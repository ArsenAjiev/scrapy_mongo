import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["omo_database"]
my_collection = my_db["products"]

for my_data in my_collection.find():
    print(my_data)
