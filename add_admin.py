
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
            
def add_admin():
    """Add the admin account"""
    
    admin_data = {
        "username": "sas admin",
        "password": "password123",
        "email": "admin@ammuchi.com"
    }
    
    print("=" * 50)
    print("Adding Admin Account to MongoDB")
    print("=" * 50)
    
    try:
        # Check if admin already exists
        existing_admin = Admin.objects(username=admin_data["username"]).first()
        if existing_admin:
            print(f"✗ Admin with username '{admin_data['username']}' already exists!")
            return False
        
        # Hash the password for security
        hashed_password = generate_password_hash(admin_data["password"])
        
        # Create new admin
        admin = Admin(
            username=admin_data["username"],
            password=hashed_password,
            email=admin_data["email"]
        )
        admin.save()
        
        print(f"\n✓ Admin account added successfully!")
        print(f"  Username: {admin_data['username']}")
        print(f"  Email: {admin_data['email']}")
        print(f"  Password: {admin_data['password']}")
        print(f"\nYou can now login at:")
        print(f"  http://127.0.0.1:5000/admin")
        
        return True
        
    except Exception as e:
        print(f"✗ Error adding admin: {str(e)}")
        return False

if __name__ == "__main__":
    add_admin()
# Hello