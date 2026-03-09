from models import User
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
connect(host=MONGODB_URI)

# Delete all users and create fresh test users
User.objects.delete()

# Create test user with plain text password (for quick testing)
test_user = User(
    name='Test User',
    email='test@example.com',
    password='password123'  # Plain text for now
)
test_user.save()

print('✓ Test user created!')
print('Email: test@example.com')
print('Password: password123')

# List all users
print(f'\nTotal users: {User.objects.count()}')
for u in User.objects:
    print(f'  - {u.email} ({u.name})')
