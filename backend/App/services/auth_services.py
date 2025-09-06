from utils.db import users_collection
import bcrypt
import time
def signup(username: str, password: str):
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return {"success": False, "message": " already exUsernameists"}

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

def login(username: str,password:str,db: str):
    try:
        user = user_collection.find_one({"username":username})
        if not user:
            return {
                "success":False,
                "message":"Username not found"
            }
        stored_hashed_password = user["password"]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            return {
                "success":True,
                "message":"Successfully logged in Twin",
                "uid":user["uid"],
                "username":user["username"]
                    }      
        else:
            return{
                "success":False,
                "message":"get your sorry ahh somewhere else"
            }
    except Exception as e: 
        return {
            "success":False,
            "message":f"Login error: {str(e)}"
        }
