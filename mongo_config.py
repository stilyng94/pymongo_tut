import pymongo
from pymongo import MongoClient

client: MongoClient = pymongo.MongoClient(host="localhost", port=27017, tz_aware=True)

db = client["dealer"]

users = db.users
cars = db.cars
