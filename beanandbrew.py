from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "anamazinglysecretkeythatnoonewilleverworkoutbecauseitssosecureandnoonewilleverfinditwatchme@123"  # This is for flash messages that will be used

# Helper function to connect to database
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def Home():
    return render_template("Home.HTML")

@app.route("/website2")
def website2():
    return render_template("Website2.HTML")

@app.route("/Hamper")
def HamperPurchasing():
    return render_template("HamperPurchasing.HTML")

@app.route("/Lesson")
def BakingLessons():
    return render_template("BakingLessons.HTML")

@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username_or_email = request.form["uname"]
        password = request.form["psw"]

        conn = get_db_connection()
        # allow login with either username or email
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? OR email = ?",
            (username_or_email, username_or_email),
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            # login success → store in session
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))  # or your homepage route
        else:
            flash("Invalid username/email or password.", "danger")
            return redirect(url_for("login"))

    # GET request → show login form
    return render_template("login.html")

@app.route("/Register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        forename = request.form["forename"]
        surname = request.form["surname"]
        email = request.form["email"]
        username = request.form["uname"]
        password = request.form["psw"]

        # Hash password before storing (for security)
        hashed_password = generate_password_hash(password)

        try:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO users (forename, surname, email, username, password) VALUES (?, ?, ?, ?, ?)",
                (forename, surname, email, username, hashed_password),
            )
            conn.commit()
            conn.close()

            flash("Account created successfully! You can now log in.", "success")
            return redirect(url_for("LoginPage"))

        except sqlite3.IntegrityError:
            flash("Username or email already exists. Please try again.", "danger")
            return redirect(url_for("register"))

    return render_template("register.HTML")  # your template file

@app.route("/BakedGoods")
def BakedGoods():
    return render_template("BakedGoods.HTML")

@app.route("/Support")
def Support():
    return render_template("Support.HTML")

@app.route("/RestaurantBooking")
def RestaurantBooking():
    return render_template("RestaurantBooking.HTML")

@app.route("/TermsAndConditions")
def TermsAndConditions():
    return render_template("TermsAndConditions.HTML")

if __name__=="__main__": # Make's it so when you run the website and make changes, you don't have to restart it
    app.run(debug=True)

