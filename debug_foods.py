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

foods = Food.objects()
print(f"\nTotal foods in database: {len(foods)}\n")
for food in foods:
    print(f"Name: {food.name}")
    print(f"Price: ₹{food.price}")
    print(f"Image URL: {food.image_url}")
    print("-" * 50)
