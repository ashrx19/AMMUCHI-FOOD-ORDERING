from mongoengine import Document, StringField, IntField, EmailField, DateTimeField
from datetime import datetime

class User(Document):
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, max_length=100)
    meta = {'collection': 'users'}

class Food(Document):
    name = StringField(required=True, max_length=100)
    price = IntField(required=True)
    category = StringField(required=True, max_length=50)
    image_url = StringField(required=False, default="/static/images/default-food.png")  # Default image if none provided
    veg_type = StringField(required=True, max_length=20, default="Veg")  # "Veg" or "Non-Veg"
    weekly_special = StringField(required=False, max_length=50)  # Day of week (e.g., "Monday", "Tuesday", or empty)
    meta = {'collection': 'foods'}

class Order(Document):
    user_id = StringField(required=True)
    items = StringField(required=True)
    customization = StringField(required=False)  # Stores cooking requests/special notes
    total = IntField(required=True)
    status = StringField(default="Placed")
    created_at = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'orders'}

class Admin(Document):
    username = StringField(required=True, unique=True, max_length=100)
    password = StringField(required=True, max_length=255)
    email = EmailField(required=False)
    created_at = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'admins'}
