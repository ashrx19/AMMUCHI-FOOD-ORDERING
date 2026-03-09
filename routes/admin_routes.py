from flask import Blueprint, render_template, request, redirect, session
from models import Food, Order, Admin
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
import os
from pathlib import Path

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# ---------------- ADMIN LOGIN ----------------
@admin_bp.route("/", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = request.form.get("password")
            
            admin = Admin.objects(username=username).first()
            
            if admin and check_password_hash(admin.password, password):
                session.clear()
                session["admin"] = True
                session["admin_id"] = str(admin.id)
                return redirect("/admin/orders")
            else:
                return render_template("admin/admin_login.html", error="Invalid credentials")
        except Exception as e:
            print(f"Admin login error: {str(e)}")
            return render_template("admin/admin_login.html", error="Database connection error. Please try again.")
    
    return render_template("admin/admin_login.html")


# ---------------- ADMIN VIEW ALL ORDERS ----------------
@admin_bp.route("/orders")
def admin_orders():
    if "admin" not in session:
        return redirect("/admin")

    orders = Order.objects()
    return render_template("admin/admin_orders.html", orders=orders)


# ---------------- UPDATE ORDER STATUS ----------------
@admin_bp.route("/update-status/<order_id>", methods=["POST"])
def update_status(order_id):
    if "admin" not in session:
        return redirect("/admin")

    order = Order.objects(id=order_id).first()
    if order:
        order.status = request.form["status"]
        order.save()

    return redirect("/admin/orders")


# ---------------- ADMIN ADD FOOD ----------------
@admin_bp.route("/add-food", methods=["GET", "POST"])
def add_food():
    if "admin" not in session:
        return redirect("/admin")

    error = None
    success = None
    
    if request.method == "POST":
        try:
            name = request.form.get("name", "").strip()
            price = request.form.get("price", "").strip()
            category = request.form.get("category", "").strip()
            veg_type = request.form.get("veg_type", "Veg").strip()
            weekly_special = request.form.get("weekly_special", "").strip()
            
            # Validate inputs
            if not name or not price or not category or not veg_type:
                error = "All fields are required"
            elif not price.isdigit() or int(price) <= 0:
                error = "Price must be a positive number"
            else:
                image_url = "/static/images/default-food.png"
                
                # Handle file upload
                if 'photo' in request.files and request.files['photo'].filename != '':
                    photo = request.files['photo']
                    if photo and allowed_file(photo.filename):
                        # Get file extension
                        ext = os.path.splitext(photo.filename)[1]
                        # Create filename: foodname.extension
                        filename = secure_filename(name.lower().replace(" ", "_")) + ext
                        filepath = os.path.join(get_upload_folder(), filename)
                        
                        # Save the file
                        photo.save(filepath)
                        image_url = f"/static/images/{filename}"
                    else:
                        error = "Invalid file format. Please upload an image."
                        foods = Food.objects()
                        return render_template("admin/admin_add_food.html", foods=foods, error=error)
                
                # Handle manually provided image URL
                manual_url = request.form.get("image_url", "").strip()
                if manual_url and manual_url != "/static/images/default-food.png":
                    image_url = manual_url
                
                food = Food(
                    name=name,
                    price=int(price),
                    category=category,
                    veg_type=veg_type,
                    weekly_special=weekly_special if weekly_special else "",
                    image_url=image_url
                )
                food.save()
                success = f"✓ Food '{name}' added successfully!"
                
        except Exception as e:
            error = f"Error adding food: {str(e)}"

    foods = Food.objects()
    return render_template("admin/admin_add_food.html", foods=foods, error=error, success=success)


# Helper functions for file upload
def allowed_file(filename):
    """Check if file extension is allowed"""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_upload_folder():
    """Get the upload folder path"""
    # Get the static/images folder relative to the app root
    upload_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')
    
    # Create folder if it doesn't exist
    os.makedirs(upload_folder, exist_ok=True)
    
    return upload_folder


# ---------------- ADMIN LOGOUT ----------------
@admin_bp.route("/logout")
def admin_logout():
    session.clear()
    return redirect("/")
