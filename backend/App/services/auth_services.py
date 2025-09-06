from utils.db import users_collection
import bcrypt
import time
def signup(username: str, password: str):

    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return {"success": False, "message": "Username already exists"}

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)  # ✅ This is correct

    uid = int(time.time()*100)%1000000
    while users_collection.find_one({"uid":uid}):
        uid += 1
    user_document = {
        "uid":uid,
        "username": username,
        "password": hashed_password.decode('utf-8')  # Converts to readable hash string
    }

    # Insert into MongoDB
    users_collection.insert_one(user_document)
    return {"success": True, "message": f"Successfully signed up with UID:{uid}",
        "uid":uid}

