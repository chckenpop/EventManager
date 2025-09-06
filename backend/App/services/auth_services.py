from App.utils.db import users_collection
import bcrypt
ALGORITHM = "HS256"

def signup(username: str,password: str,db):
    #signup logic like insert the username and password into the db hash the password too ts simple af
    existing_user = users_collection.find_one({"username":username})
    if existing_user:
        return {"message": "successfully signedup"}
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"),salt)
    user_document = {
        "username":username,
        "password":hashed_password
    }
    result = users_collection.insert_one(user_document)
    if result.inserted_id:
        return {"message": "successfully signedup"}
    else:
        return{"message": "lol bozo"}
def login(username: str,password:str,db: str):
    #login logic check if exists 
    
    
    return {"message": "sucessfully locked in"}

