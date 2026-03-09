from flask import Flask
from dotenv import load_dotenv
from routes import user_bp, admin_bp
import os
from mongoengine import connect
import sys

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = "ammuchi_secret"

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'images')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# MongoDB Atlas Configuration
MONGODB_URI = os.getenv('MONGODB_URI')

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in environment variables. Please check your .env file.")

# Connect to MongoDB with retry logic
try:
    print("Connecting to MongoDB Atlas...")
    connect(
        host=MONGODB_URI,
        connectTimeoutMS=60000,  # 60 seconds
        serverSelectionTimeoutMS=60000,  # 60 seconds
        socketTimeoutMS=60000,  # 60 seconds
        retryWrites=True,
        w='majority'
    )
    print("✓ Connected to MongoDB Atlas successfully!")
except Exception as e:
    print(f"\n✗ Error connecting to MongoDB Atlas: {str(e)}")
    print("\nPossible solutions:")
    print("1. Check your internet connection")
    print("2. Verify MongoDB Atlas cluster is running (not paused)")
    print("3. Check if your IP is whitelisted in MongoDB Atlas")
    print("4. Verify the connection string in .env file")
    print("\nTroubleshooting steps:")
    print("- Go to MongoDB Atlas → Security → Network Access")
    print("- Add your current IP address to the whitelist")
    print("- Or add 0.0.0.0/0 to allow all IPs (not recommended for production)")
    sys.exit(1)

app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
