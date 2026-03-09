"""
Script to add sample food items to MongoDB
This will create the 'foods' collection automatically
"""

from dotenv import load_dotenv
import os
from mongoengine import connect
from models import Food

# Load environment variables
load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in environment variables. Please check your .env file.")

# Connect to MongoDB
connect(host=MONGODB_URI)

def add_sample_foods():
    """Add sample food items to create the foods collection"""
    
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
    
    print("=" * 50)
    print("Creating Foods Collection")
    print("=" * 50)
    
    try:
        print("\n🍱 Adding sample food items...")
        
        for food_data in foods_data:
            # Check if food already exists
            if not Food.objects(name=food_data["name"]).first():
                food = Food(**food_data)
                food.save()
                print(f"  ✓ {food_data['name']} (₹{food_data['price']}) - {food_data['category']}")
            else:
                print(f"  ⚠ {food_data['name']} already exists")
        
        print("\n✓ Foods collection created successfully!")
        print("\nYou can now:")
        print("  1. Go to: http://127.0.0.1:5000/menu")
        print("  2. Login with any user account")
        print("  3. See all the food items")
        print("\nOr add more items in admin panel:")
        print("  Go to: http://127.0.0.1:5000/admin/add-food")
        
        return True
        
    except Exception as e:
        print(f"✗ Error creating foods collection: {str(e)}")
        return False

if __name__ == "__main__":
    add_sample_foods()
