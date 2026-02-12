"""
Script to clean up foods and add only those with valid images
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

def cleanup_foods():
    """Delete all foods and add only good ones with images"""
    
    print("=" * 50)
    print("Cleaning Up Foods Database")
    print("=" * 50)
    
    # Delete all foods
    count = Food.objects.count()
    Food.drop_collection()
    print(f"✓ Deleted all {count} foods")
    
    # Add only foods with proper images
    foods_data = [
        {
            "name": "Biryani",
            "price": 250,
            "category": "Rice",
            "image_url": "https://images.unsplash.com/photo-1584584867912-726e5b3b6a2b?w=400"
        },
        {
            "name": "Butter Chicken",
            "price": 290,
            "category": "Curry",
            "image_url": "https://images.unsplash.com/photo-1585937421293-7f325fc8486c?w=400"
        },
        {
            "name": "Samosa",
            "price": 60,
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
        },
        {
            "name": "Chicken 65",
            "price": 140,
            "category": "Non-Veg",
            "image_url": "https://images.unsplash.com/photo-1626082927389-6cd097cda687?w=400"
        },
        {
            "name": "Gobi Fry",
            "price": 110,
            "category": "Veg",
            "image_url": "https://images.unsplash.com/photo-1599599810694-b3b146f179d7?w=400"
        }
    ]
    
    print("\n" + "=" * 50)
    print("Adding Clean Foods with Images")
    print("=" * 50)
    
    for food_data in foods_data:
        food = Food(**food_data)
        food.save()
        print(f"✓ {food_data['name']} (₹{food_data['price']})")
    
    print("\n" + "=" * 50)
    print(f"✓ Added {len(foods_data)} foods with images!")
    print("=" * 50)
    print("\nNow:")
    print("  1. Refresh your browser: http://127.0.0.1:5000/menu")
    print("  2. You should see all foods with images!")

if __name__ == "__main__":
    cleanup_foods()
