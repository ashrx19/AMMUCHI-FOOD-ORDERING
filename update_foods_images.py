"""
Script to update all food items with images
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

def update_foods_with_images():
    """Update all foods with image URLs"""
    
    # Map of food names to JPEG image files
    food_images = {
        "Biryani": "/static/images/biryani.jpeg",
        "Butter Chicken": "/static/images/dessert.jpeg",
        "Samosa": "/static/images/bread.jpg",
        "Paneer Tikka": "/static/images/salad.jpeg",
        "Gulab Jamun": "/static/images/cake.jpg",
        "Mango Lassi": "/static/images/pastry.jpg",
        "Masala Dosa": "/static/images/pasta.jpeg",
        "Tandoori Chicken": "/static/images/hero_food.jpg",
        "Chicken 65": "/static/images/dessert.jpeg",
        "Gobi Fry": "/static/images/salad.jpeg",
    }
    
    print("=" * 50)
    print("Updating Foods with Images")
    print("=" * 50)
    
    try:
        updated = 0
        not_found = 0
        
        for food_name, image_url in food_images.items():
            food = Food.objects(name=food_name).first()
            if food:
                food.image_url = image_url
                food.save()
                print(f"✓ Updated: {food_name}")
                updated += 1
            else:
                print(f"⚠ Not found: {food_name}")
                not_found += 1
        
        print("\n" + "=" * 50)
        print(f"✓ Updated: {updated} items")
        print(f"⚠ Not found: {not_found} items")
        print("=" * 50)
        print("\nNow refresh your browser:")
        print("  http://127.0.0.1:5000/menu")
        
        return True
        
    except Exception as e:
        print(f"✗ Error updating foods: {str(e)}")
        return False

if __name__ == "__main__":
    update_foods_with_images()
