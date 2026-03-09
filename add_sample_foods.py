"""
Script to add sample food items with images to the menu
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
connect(host=MONGODB_URI, connectTimeoutMS=60000, serverSelectionTimeoutMS=60000, socketTimeoutMS=60000)

def add_sample_foods_with_images():
    """Add sample food items with image URLs"""
    
    # Using external image URLs from free services
    foods_data = [
        {
            "name": "Biryani",
            "price": 250,
            "category": "Rice",
            "image_url": "https://images.unsplash.com/photo-1584584867912-726e5b3b6a2b?w=400"
        },
        {
            "name": "Butter Chicken",
            "price": 350,
            "category": "Curry",
            "image_url": "https://images.unsplash.com/photo-1585937421293-7f325fc8486c?w=400"
        },
        {
            "name": "Samosa",
            "price": 50,
            "category": "Appetizer",
            "image_url": "https://images.unsplash.com/photo-1619984920406-67d7a76a1e2d?w=400"
        },
        {
            "name": "Paneer Tikka",
            "price": 200,
            "category": "Appetizer",
            "image_url": "https://images.unsplash.com/photo-1599599810694-b3b146f179d7?w=400"
        },
        {
            "name": "Gulab Jamun",
            "price": 80,
            "category": "Dessert",
            "image_url": "https://images.unsplash.com/photo-1585960453919-e21cc028cb29?w=400"
        },
        {
            "name": "Mango Lassi",
            "price": 100,
            "category": "Beverage",
            "image_url": "https://images.unsplash.com/photo-1585936687183-e0a0eba5e8b8?w=400"
        },
        {
            "name": "Masala Dosa",
            "price": 150,
            "category": "Breakfast",
            "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400"
        },
        {
            "name": "Tandoori Chicken",
            "price": 300,
            "category": "Main Course",
            "image_url": "https://images.unsplash.com/photo-1599599810694-b3b146f179d7?w=400"
        }
    ]
    
    print("=" * 50)
    print("Adding Sample Foods with Images")
    print("=" * 50)
    
    try:
        added = 0
        skipped = 0
        
        for food_data in foods_data:
            # Check if food already exists
            if not Food.objects(name=food_data["name"]).first():
                food = Food(**food_data)
                food.save()
                print(f"✓ {food_data['name']} (₹{food_data['price']}) - {food_data['category']}")
                added += 1
            else:
                print(f"⚠ {food_data['name']} already exists (skipped)")
                skipped += 1
        
        print("\n" + "=" * 50)
        print(f"✓ Added: {added} items")
        print(f"⚠ Skipped: {skipped} items (already exist)")
        print("=" * 50)
        print("\nYou can now:")
        print("  1. Go to: http://127.0.0.1:5000/menu")
        print("  2. Login and see all foods with images!")
        print("  3. Visit admin panel to add more foods")
        
        return True
        
    except Exception as e:
        print(f"✗ Error adding foods: {str(e)}")
        return False

if __name__ == "__main__":
    add_sample_foods_with_images()
