from models import Food
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
connect(host=MONGODB_URI)

# Map database food names to image file names
image_mapping = {
    'Biryani': '/static/images/briyani.jpeg',
    'Butter Chicken': '/static/images/butter chicken.jpeg',
    'Paneer Tikka': '/static/images/panner tikka.jpeg',
    'Gulab Jamun': '/static/images/gulab jammun.jpeg',
    'Mango Lassi': '/static/images/mango lassi.jpeg',
    'Masala Dosa': '/static/images/masal Dosa.jpeg',
    'Tandoori Chicken': '/static/images/tandoori chicken.jpeg',
    'Chicken 65': '/static/images/chicken 65.jpeg',
    'Gobi Fry': '/static/images/gobi 65.jpeg',
    'Samosa': '/static/images/chappati.jpeg',  # Using Chapati for Samosa
}

print('🔄 Updating Food Images in Database...\n')

# Update food items with image URLs
updated_count = 0
for food_name, image_url in image_mapping.items():
    food = Food.objects(name=food_name).first()
    if food:
        food.image_url = image_url
        food.save()
        print(f'✓ {food.name:<20} → {image_url}')
        updated_count += 1
    else:
        print(f'✗ Not found: {food_name}')

print(f'\n✅ Successfully updated {updated_count}/{len(image_mapping)} food items')

print('\n📋 Final Food List with Images:')
print('-' * 70)
foods = Food.objects()
for food in foods:
    status = '✓' if 'static/images' in food.image_url else '○'
    print(f'{status} {food.name:<20} | {food.veg_type:<10} | ₹{food.price:<5} | {food.image_url}')
