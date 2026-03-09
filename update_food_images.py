from models import Food
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
connect(host=MONGODB_URI)

# Map food names to image file names
image_mapping = {
    'Biryani': '/static/images/briyani.jpeg',
    'Butter Chicken': '/static/images/butter chicken.jpeg',
    'Chapati': '/static/images/chappati.jpeg',
    'Chicken 65': '/static/images/chicken 65.jpeg',
    'Egg Parotta': '/static/images/egg parotta.jpeg',
    'Gobi 65': '/static/images/gobi 65.jpeg',
    'Gulab Jamun': '/static/images/gulab jammun.jpeg',
    'Mango Lassi': '/static/images/mango lassi.jpeg',
    'Masala Dosa': '/static/images/masal Dosa.jpeg',
    'Paneer Tikka': '/static/images/panner tikka.jpeg',
    'Pasta': '/static/images/pasta.jpeg',
    'Tandoori Chicken': '/static/images/tandoori chicken.jpeg',
}

# Update food items with image URLs
updated_count = 0
for food_name, image_url in image_mapping.items():
    food = Food.objects(name__iexact=food_name).first()
    if food:
        food.image_url = image_url
        food.save()
        print(f'✓ Updated: {food.name} → {image_url}')
        updated_count += 1
    else:
        print(f'✗ Not found: {food_name}')

print(f'\n✓ Total updated: {updated_count} food items')

# List all foods with their image URLs
print('\n--- All Foods with Images ---')
foods = Food.objects()
for food in foods:
    print(f'{food.name} ({food.veg_type}): {food.image_url}')
