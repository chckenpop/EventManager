import sys
import os

# Add paths for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, '..'))

from utils.db import users_collection
import bcrypt

def check_username(username: str):
    """Check if username exists in database"""
    user = users_collection.find_one({"username": username})
    return user is not None

def login(username: str, password: str):
    # Find user in database
    user = users_collection.find_one({"username": username})
    
    # Check password
    stored_password = user["password"]
    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        return {
            "success": True, 
            "message": "Successfully logged in", 
            "uid": user["uid"], 
            "username": user["username"]
        }
    else:
        return {"success": False, "message": "Incorrect password"}

# Simple manual test
if __name__ == "__main__":
    print("=== LOGIN TEST ===")
    
    # Step 1: Check username first
    username = input("Enter username: ")
    
    if not check_username(username):
        print("FAILED: Username not found")
        print("Please check your username and try again.")
    else:
        # Step 2: Only ask for password if username exists
        password = input("Enter password: ")
        
        result = login(username, password)
        
        if result["success"]:
            print("SUCCESS:", result["message"])
            print("Welcome", result["username"])
            print("Your UID:", result["uid"])
        else:
            print("FAILED:", result["message"])
