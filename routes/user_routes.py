from flask import Blueprint, render_template, request, redirect, session
from models import User, Food, Order
from werkzeug.security import check_password_hash, generate_password_hash

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def home():
    # Get weekly specials
    weekly_specials = Food.objects(weekly_special__ne="").limit(6)
    return render_template("user/home_new.html", weekly_specials=weekly_specials)

@user_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        try:
            # Hash the password before storing
            hashed_password = generate_password_hash(request.form["password"])
            user = User(
                name=request.form["name"],
                email=request.form["email"],
                password=hashed_password
            )
            user.save()
            return redirect("/login")
        except Exception as e:
            return render_template("user/signup.html", error="Email already exists")
    return render_template("user/signup.html")

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.objects(email=email).first()
        
        if user:
            # Try hashed password first (new users)
            if check_password_hash(user.password, password):
                session.clear()
                session["user_id"] = str(user.id)
                return redirect("/menu")
            # Fall back to plain text comparison (for manually added users)
            elif user.password == password:
                session.clear()
                session["user_id"] = str(user.id)
                return redirect("/menu")
        
        return render_template("user/login.html", error="Invalid credentials")
    return render_template("user/login.html")

@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@user_bp.route("/menu")
def menu():
    if "user_id" not in session and "admin" not in session:
        return redirect("/login")
    foods = Food.objects()
    return render_template("user/menu.html", foods=foods)

@user_bp.route("/order", methods=["POST"])
def place_order():
    if "user_id" not in session:
        return redirect("/login")

    items = ", ".join(request.form.getlist("items"))
    customization = request.form.get("customization", "")
    total = request.form.get("total", 0)

    order = Order(
        user_id=session["user_id"],
        items=items,
        customization=customization,
        total=int(total)
    )
    order.save()
    return redirect("/orders")

@user_bp.route("/orders")
def orders():
    if "admin" in session:
        return redirect("/menu")
    if "user_id" not in session:
        return redirect("/login")

    orders = Order.objects(user_id=session["user_id"])
    return render_template("user/orders.html", orders=orders)
