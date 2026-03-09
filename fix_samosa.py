from models import Food
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
connect(host=MONGODB_URI)

samosa = Food.objects(name='Samosa').first()
if samosa:
    samosa.image_url = '/static/images/samosa.jpeg'
    samosa.save()
    print('✓ Updated: Samosa → /static/images/samosa.jpeg')
    
    # Verify
    updated = Food.objects(name='Samosa').first()
    print(f'✓ Verified: {updated.image_url}')
