from flask import Flask, render_template, request, redirect, session
from cs50 import SQL
from flask_session import Session

app = Flask(__name__)
app.secret_key = "skillTimey"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///skillTimey.db")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if both fields are filled
        if not username or not password:
            return "Username and password required."

        # Check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?",username)
        if len(rows) != 0:
            return "Username already exists."

        # Insert into database
        db.execute("INSERT INTO users (username,password) VALUES (?,?)",username,password)

        # Get the new user ID
        new_user = db.execute("SELECT id FROM users WHERE username = ?",username)
        session["user_id"] = new_user[0]["id"]

        return redirect("/profile")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check for user in DB
        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        if not user or user[0]["password"] != password:
            return "Invalid username or password."

        # Login successful
        session["user_id"] = user[0]["id"]
        return redirect("/dashboard")

    return render_template("login.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        nickname = request.form.get("nickname")
        qualification = request.form.get("qualification") or request.form.get("qualification-level")
        age = request.form.get("age")
        cgpa = request.form.get("cgpa") or None
        interests = request.form.get("interests")
        course = request.form.get("course")
        year = request.form.get("year")  # Only available if status == Pursuing

        db.execute("INSERT INTO profiles (user_id, nickname, qualification, course, year, cgpa, interests) VALUES (?, ?, ?, ?, ?, ?, ?)",
           session["user_id"], nickname, qualification, course, year, cgpa, interests)

        return redirect("/dashboard")  

    return render_template("profile.html")

@app.route("/dashboard")
def dashboard():
    user_id = session.get("user_id")
    if not user_id:
        return redirect("/login")

    # Fetch the profile of the logged-in user
    profile = db.execute("SELECT * FROM profiles WHERE user_id = ?", user_id)

    if not profile:
        return redirect("/profile")

    return render_template("dashboard.html", profile=profile[0])

@app.route("/goals")
def goals():
    if "user_id" not in session:
        return redirect("/login")

    profile = db.execute("SELECT * FROM profiles WHERE user_id = ?", session["user_id"])
    return render_template("goals.html", profile=profile[0])

@app.route("/skills")
def skills():
    if "user_id" not in session:
        return redirect("/login")

    profile = db.execute("SELECT * FROM profiles WHERE user_id = ?", session["user_id"])
    return render_template("skills.html", profile=profile[0])

@app.route("/suggestions")
def suggestions():
    if "user_id" not in session:
        return redirect("/login")

    profile = db.execute("SELECT * FROM profiles WHERE user_id = ?", session["user_id"])
    return render_template("suggestions.html", profile=profile[0])

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        nickname = request.form.get("nickname")
        interests = request.form.get("interests")
        cgpa = request.form.get("cgpa")
        year = request.form.get("year")

        db.execute("""
            UPDATE profiles
            SET nickname = ?, interests = ?, cgpa = ?, year = ?
            WHERE user_id = ?
        """, nickname, interests, cgpa, year, session["user_id"])

        return redirect("/dashboard")

    # GET method: show current values
    profile = db.execute("SELECT * FROM profiles WHERE user_id = ?", session["user_id"])
    return render_template("settings.html", profile=profile[0])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Some suggestions and code snippets were guided by ChatGPT. All final implementation is my own.
