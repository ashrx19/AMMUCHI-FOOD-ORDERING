# 🖼️ How to Add Food Images

## Step 1: Place Image Files in the Correct Folder

Your images should go in: `static/images/`

**Full path:** `ammuchi_food_ordering/static/images/`

## Step 2: Supported Image Formats
- JPG/JPEG (`.jpg`, `.jpeg`)
- PNG (`.png`)
- WebP (`.webp`)
- GIF (`.gif`)


Example filenames:
- `biryani.jpg`
- `butter-chicken.png`
- `samosa.jpg`

## Step 3: Add Food with Image URL

### Option A: Using Admin Panel
1. Go to `http://127.0.0.1:5000/admin/add-food`
2. Fill in the form:
   - **Food Name:** Biryani
   - **Price:** 250
   - **Category:** Rice
   - **Image URL:** `/static/images/biryani.jpg`
3. Click "Add Food"

### Option B: Using MongoDB Directly
Update the food document with image_url field:
```json
{
  "name": "Biryani",
  "price": 250,
  "category": "Rice",
  "image_url": "/static/images/biryani.jpg"
}
```

## Step 4: Examples

**Food with custom image:**
```
Image URL: /static/images/butter-chicken.jpg
```

**Default image (if you don't provide one):**
```
Image URL: /static/images/default-food.png
```

## Step 5: View Your Images

After adding food items, they will appear with images in:
- **User Menu:** `http://127.0.0.1:5000/menu`
- **Admin Panel:** `http://127.0.0.1:5000/admin/add-food`

## 📝 Notes

- Make sure image files are actually in `static/images/` folder
- Use relative paths like `/static/images/filename.jpg`
- If image doesn't load, check if the filename and path are correct
- You can also use external URLs: `https://example.com/image.jpg`

## Example Food Items with Images

Here's a script to add sample foods with images:

```python
from models import Food
from dotenv import load_dotenv
import os
from mongoengine import connect

load_dotenv()
connect(host=os.getenv('MONGODB_URI'))

foods = [
    {"name": "Biryani", "price": 250, "category": "Rice", "image_url": "/static/images/biryani.jpeg"},
    {"name": "Butter Chicken", "price": 350, "category": "Curry", "image_url": "/static/images/butter-chicken.jpg"},
    {"name": "Samosa", "price": 50, "category": "Appetizer", "image_url": "/static/images/samosa.jpg"},
]

for food_data in foods:
    if not Food.objects(name=food_data["name"]).first():
        food = Food(**food_data)
        food.save()
        print(f"Added {food_data['name']}")
```

Done! Your food items will now display with beautiful images! 🍽️✨
