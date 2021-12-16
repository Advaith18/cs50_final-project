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
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
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
            password_hashed = generate_password_hash(password)
            db.execute("INSERT INTO users(username, password_hash) VALUES(?, ?)", username, password_hashed)
            return redirect("/login")


@app.route("/logout", methods = ["POST", "GET"])
def logout():
    session.clear()
    return redirect("/login")


@app.route("/beginners", methods = ["POST", "GET"])
def beginners():
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("beginners.html")

@app.route("/intermediate", methods = ["POST", "GET"])
def intermediate():
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("intermediate.html")


@app.route("/fastest", methods = ["POST", "GET"])
def fastest():
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("fastest.html")


@app.route("/looks", methods = ["POST", "GET"])
def looks():
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("looks.html")

@app.route("/beautiful", methods = ["POST", "GET"])
def beautiful():
    if not session.get("user_id"):
        return redirect("index.html")
    return render_template("beautifyl.html")
