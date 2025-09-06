# simple_signup.py (place in backend/App folder)
import sys
import os

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from services.auth_services import signup

def main():
    print("=" * 40)
    print("    USER REGISTRATION SYSTEM")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Sign up new user")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1 or 2): ")
        
        if choice == "1":
            print("\n--- CREATE NEW ACCOUNT ---")
            username = input("Enter username: ")
            password = input("Enter password: ")
            
            if not username or not password:
                print("Error: Username and password cannot be empty!")
                continue
            
            print(f"\nCreating account for '{username}'...")
            result = signup(username, password)
            
            if result["success"]:
                print("SUCCESS: " + result['message'])
                print("Check MongoDB Compass to see your user!")
            else:
                print("ERROR: " + result['message'])
                
        elif choice == "2":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
if __name__ == "__main__":
    main()
