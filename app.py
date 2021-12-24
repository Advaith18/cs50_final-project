from cs50 import SQL
from flask import Flask, render_template, redirect, session, request, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///finance.db")

@app.route("/", methods = ["POST", "GET"])
def index():
    # Checking if user logged in or not.
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Checking if user is present in the database.
        user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if not user:
            return render_template("apology.html", apology="username_not")
        elif user:
            rows = db.execute("SELECT id FROM users WHERE username = ?", username)
            hashed = db.execute("SELECT password_hash FROM users WHERE id = ?", rows[0]["id"])
            if not check_password_hash(hashed[0]["password_hash"], password):
                return render_template("apology.html", apology = "password_hash")
            
            session["user_id"] = rows[0]["id"]
            return redirect("/")
    elif request.method == "GET":
        return render_template("login.html")


@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Checking if username is already there in the database.
        username_existance = db.execute("SELECT * FROM users WHERE username  = ?", username)
        if not username:
            return render_template("apology.html", apology="no_username")
        elif not password:
            return render_template("apology.html", apology="no_password")
        elif not confirmation:
            return render_template("apology.html", apology="no_confirmation")
        elif confirmation != password:
            return render_template("apology.html", apology="no_match")
        elif username_existance:
            return render_template("apology.html", apology = "username_exists")
        else:
            # Hashing the password provided byy the user.
            password_hashed = generate_password_hash(password)
            # Inserting user into database..
            db.execute("INSERT INTO users(username, password_hash) VALUES(?, ?)", username, password_hashed)
            return redirect("/login")


@app.route("/logout", methods = ["POST", "GET"])
def logout():
    # clearing sessions.
    session.clear()
    return redirect("/login")


@app.route("/beginners", methods = ["POST", "GET"])
def beginners():
    # Checking if user logged in or not.
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("beginners.html")

@app.route("/intermediate", methods = ["POST", "GET"])
def intermediate():
    # Checking if user logged in or not.
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("intermediate.html")


@app.route("/fastest", methods = ["POST", "GET"])
def fastest():
    # Checking if user logged in or not.
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("fastest.html")


@app.route("/looks", methods = ["POST", "GET"])
def looks():
    # Checking if user logged in or not.
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("looks.html")

@app.route("/beautiful", methods = ["POST", "GET"])
def beautiful():
    # Checking if user logged in or not.
    if not session.get("user_id"):
        return redirect("index.html")
    return render_template("beautiful.html")


@app.route("/about_us", methods = ["POST", "GET"])
def about_us():
    # Checking if user logged in or not.
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("about_us.html")


@app.route("/feedback", methods = ["POST", "GET"])
def feedback():
    if request.method == "GET":
        # Checking if user logged in or did not login.
        if not session.get("user_id"):
            return redirect("/login")
        # Getting username from users table using SQL function from cs50 library which is very nice.
        username = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
        return render_template("feedback.html", username = username)
    else:
        username = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
        feedback = request.form.get("hidden")
        db.execute("INSERT INTO feedbacks(user_id, username, feedback) VALUES(?, ?, ?);", session["user_id"], username, feedback)
        return render_template("feedback.html", username = username)
