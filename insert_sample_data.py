"""
Script to insert sample data into MongoDB collections
"""

from dotenv import load_dotenv
import os
from mongoengine import connect
from models import User, Food, Order, Admin
from werkzeug.security import generate_password_hash

# Load environment variables
load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in environment variables. Please check your .env file.")

# Connect to MongoDB
connect(host=MONGODB_URI)

def insert_sample_data():
    """Insert sample data into the database"""
    
    print("=" * 50)
    print("Inserting Sample Data")
    print("=" * 50)
    
    # Clear existing data (optional - comment out if you want to keep existing data)
    # User.drop_collection()
    # Food.drop_collection()
    # Order.drop_collection()
    
    try:
        # Sample Users
        users_data = [
            {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "password123"
            },
            {
                "name": "Jane Smith",
                "email": "jane@example.com",
                "password": "password456"
            },
            {
                "name": "Bob Johnson",
                "email": "bob@example.com",
                "password": "password789"
            }
        ]
        
        print("\n📝 Adding Users...")
        for user_data in users_data:
            # Check if user already exists
            if not User.objects(email=user_data["email"]).first():
                user = User(**user_data)
                user.save()
                print(f"  ✓ User '{user_data['name']}' added")
            else:
                print(f"  ⚠ User '{user_data['email']}' already exists")
        
        # Sample Foods
        foods_data = [
            {
                "name": "Biryani",
                "price": 250,
                "category": "Rice"
            },
            {
                "name": "Butter Chicken",
                "price": 350,
                "category": "Curry"
            },
            {
                "name": "Samosa",
                "price": 50,
                "category": "Appetizer"
            },
            {
                "name": "Paneer Tikka",
                "price": 200,
                "category": "Appetizer"
            },
            {
                "name": "Gulab Jamun",
                "price": 80,
                "category": "Dessert"
            },
            {
                "name": "Mango Lassi",
                "price": 100,
                "category": "Beverage"
            }
        ]
        
        print("\n🍱 Adding Foods...")
        for food_data in foods_data:
            # Check if food already exists
            if not Food.objects(name=food_data["name"]).first():
                food = Food(**food_data)
                food.save()
                print(f"  ✓ Food '{food_data['name']}' added (Rs. {food_data['price']})")
            else:
                print(f"  ⚠ Food '{food_data['name']}' already exists")
        
        print("\n✓ Sample data inserted successfully!")
        print("\nYou can now:")
        print("  1. Login to the app with:")
        print("     - Email: john@example.com")
        print("     - Password: password123")
        print("  2. Browse and order foods from the menu")
        
    except Exception as e:
        print(f"✗ Error inserting data: {str(e)}")

if __name__ == "__main__":
    insert_sample_data()
