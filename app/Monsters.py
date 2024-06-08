from MonsterLab import Monster
from pymongo import MongoClient
from certifi import where

db = MongoClient("dburl", tlsCAFile=where())["Bandersnatch"]
collection = db.get_collection("Monsters")
monsters = []
for _ in range(0, 10):
    monsters.append(Monster().to_dict())

print(monsters)

collection.insert_many(monsters)