from mongoengine import connect, Document, StringField
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

connect(
    host=MONGODB_URI,
    connectTimeoutMS=60000,
    serverSelectionTimeoutMS=60000,
    socketTimeoutMS=60000,
    retryWrites=True,
    tlsInsecure=True
)

class Food(Document):
    name = StringField(required=True)
    price = StringField(required=True)
    category = StringField(required=True)
    image_url = StringField(default="/static/images/default-food.svg")
    meta = {"collection": "foods"}

# Map foods to JPEG images
image_map = {
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

foods = Food.objects()
print(f"Updating {len(foods)} foods with JPEG images...\n")

for food in foods:
    if food.name in image_map:
        food.image_url = image_map[food.name]
        food.save()
        print(f"✓ {food.name} -> {image_map[food.name]}")
    else:
        print(f"⚠ {food.name} - no image mapping")

print("\nDone! All foods updated with real images.")
