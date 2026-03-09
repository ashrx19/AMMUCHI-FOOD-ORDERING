"""
Script to create an admin account for the first time
Run this script once to set up your admin account
"""

from dotenv import load_dotenv
import os
from mongoengine import connect
from werkzeug.security import generate_password_hash
from models import Admin

# Load environment variables
load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in environment variables. Please check your .env file.")

# Connect to MongoDB
connect(host=MONGODB_URI)

def create_admin(username, password, email=None):
    """Create a new admin account"""
    try:
        # Check if admin already exists
        existing_admin = Admin.objects(username=username).first()
        if existing_admin:
            print(f"Admin '{username}' already exists!")
            return False
        
        # Hash the password
        hashed_password = generate_password_hash(password)
        
        # Create new admin
        admin = Admin(
            username=username,
            password=hashed_password,
            email=email
        )
        admin.save()
        print(f"✓ Admin account '{username}' created successfully!")
        return True
        
    except Exception as e:
        print(f"✗ Error creating admin account: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Admin Account Setup")
    print("=" * 50)
    
    username = input("Enter admin username: ").strip()
    password = input("Enter admin password: ").strip()
    email = input("Enter admin email (optional): ").strip() or None
    
    if username and password:
        create_admin(username, password, email)
    else:
        print("✗ Username and password are required!")
