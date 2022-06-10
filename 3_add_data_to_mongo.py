import pymongo
import json

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["omo_database"]
my_collection = my_db["products"]

with open("data.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

add_data = my_collection.insert_many(data)

print(add_data.inserted_ids)
