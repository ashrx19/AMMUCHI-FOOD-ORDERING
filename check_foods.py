"""
Script to check all foods in database
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

def check_foods():
    """Check all foods in database"""
    
    print("=" * 50)
    print("Foods in Database")
    print("=" * 50)
    
    all_foods = Food.objects()
    
    if all_foods.count() == 0:
        print("No foods found in database!")
        return
    
    for food in all_foods:
        print(f"\nName: {food.name}")
        print(f"Price: ₹{food.price}")
        print(f"Category: {food.category}")
        print(f"Image URL: {food.image_url}")
        print("-" * 50)
    
    print(f"\nTotal foods: {all_foods.count()}")

if __name__ == "__main__":
    check_foods()
