from pymongo.mongo_client import MongoClient

MONGODB_USERNAME = "onlymvp"
MONGODB_PASSWORD = "password"
MONGODB_CLUSTER = ""
client = MongoClient(f'mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@43.202.53.29', 27017, tlsInsecure= True)
db = client.homey