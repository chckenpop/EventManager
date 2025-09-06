# user data 
# user events
from pymongo import MongoClient, errors
client = MongoClient("mongodb://localhost:27017")
db = client ['mydatabase']
users_collection = db["users"]
try:
    users_collection.create_index("username",unique=True)
except errors.OperationFailure:
    pass

def get_db():
    if db is None:
        raise Exception("Database connection is not established")
        return None
    return db