"""
Script to add a single user to MongoDB
"""

from dotenv import load_dotenv
import os
from mongoengine import connect
from models import User

# Load environment variables
load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in environment variables. Please check your .env file.")

# Connect to MongoDB
connect(host=MONGODB_URI)

def add_user():
    """Add the admin user"""
    
    user_data = {
        "name": "sas admin",
        "email": "admin@ammuchi.com",
        "password": "password123"
    }
    
    print("=" * 50)
    print("Adding User to MongoDB")
    print("=" * 50)
    
    try:
        # Check if user already exists
        existing_user = User.objects(email=user_data["email"]).first()
        if existing_user:
            print(f"✗ User with email '{user_data['email']}' already exists!")
            return False
        
        # Create new user
        user = User(**user_data)
        user.save()
        
        print(f"\n✓ User added successfully!")
        print(f"  Name: {user_data['name']}")
        print(f"  Email: {user_data['email']}")
        print(f"  Password: {user_data['password']}")
        print(f"\nYou can now login with these credentials at:")
        print(f"  http://127.0.0.1:5000/login")
        
        return True
        
    except Exception as e:
        print(f"✗ Error adding user: {str(e)}")
        return False

if __name__ == "__main__":
    add_user()
