from flask import Blueprint, render_template, request, redirect, session
from extensions import db
from models import User, Food, Order

routes_bp = Blueprint("routes_bp", __name__)

# ---------------- HOME ----------------
@routes_bp.route("/")
def home():
    return render_template("home.html")


# ---------------- SIGNUP ----------------
@routes_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")

    return render_template("signup.html")


# ---------------- LOGIN ----------------
@routes_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            email=request.form["email"],
            password=request.form["password"]
        ).first()

        if user:
            session["user_id"] = user.id
            return redirect("/menu")

    return render_template("login.html")


# ---------------- LOGOUT ----------------
@routes_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/")


# ---------------- MENU ----------------
@routes_bp.route("/menu")
def menu():
    if "user_id" not in session:
        return redirect("/login")

    foods = Food.query.all()
    return render_template("menu.html", foods=foods)


# ---------------- PLACE ORDER ----------------
@routes_bp.route("/order", methods=["POST"])
def place_order():
    if "user_id" not in session:
        return redirect("/login")

    selected_items = request.form.getlist("items")
    total = request.form.get("total", 0)

    order = Order(
        user_id=session["user_id"],
        items=", ".join(selected_items),
        total=total
    )
    db.session.add(order)
    db.session.commit()

    return redirect("/orders")


# ---------------- VIEW ORDERS ----------------
@routes_bp.route("/orders")
def orders():
    if "user_id" not in session:
        return redirect("/login")

    user_orders = Order.query.filter_by(
        user_id=session["user_id"]
    ).all()

    return render_template("orders.html", orders=user_orders)


# =====================================================
# ================== ADMIN SECTION ====================
# =====================================================

# ---------------- ADMIN LOGIN ----------------
@routes_bp.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Hardcoded admin credentials (for academic project)
        if username == "admin" and password == "admin123":
            session["admin"] = True
            return redirect("/admin/add-food")

    return render_template("admin_login.html")


# ---------------- ADMIN ADD FOOD ----------------
@routes_bp.route("/admin/add-food", methods=["GET", "POST"])
def admin_add_food():
    if "admin" not in session:
        return redirect("/admin")

    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        category = request.form["category"]

        food = Food(name=name, price=price, category=category)
        db.session.add(food)
        db.session.commit()

    foods = Food.query.all()
    return render_template("admin_add_food.html", foods=foods)


# ---------------- ADMIN LOGOUT ----------------
@routes_bp.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect("/")
