from models import Food
from app import app

# Connect to MongoDB via app context
with app.app_context():
    # Get all foods
    foods = Food.objects()
    
    # Map of food names to simple local SVG placeholders
    image_map = {
        "Biryani": "/static/images/biryani.svg",
        "Butter Chicken": "/static/images/butter_chicken.svg",
        "Samosa": "/static/images/samosa.svg",
        "Paneer Tikka": "/static/images/paneer_tikka.svg",
        "Gulab Jamun": "/static/images/gulab_jamun.svg",
        "Mango Lassi": "/static/images/mango_lassi.svg",
        "Masala Dosa": "/static/images/masala_dosa.svg",
        "Tandoori Chicken": "/static/images/tandoori_chicken.svg",
        "Chicken 65": "/static/images/chicken_65.svg",
        "Gobi Fry": "/static/images/gobi_fry.svg",
    }
    
    # Update each food with a local image
    for food in foods:
        if food.name in image_map:
            food.image_url = image_map[food.name]
        else:
            food.image_url = "/static/images/default-food.svg"
        food.save()
        print(f"✓ Updated {food.name} -> {food.image_url}")
    
    print("\n✓ All foods updated with local image paths!")
