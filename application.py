import os

from flask import Flask, render_template,session, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=["GET","POST"])
def index():
    username = request.form.get("username")
    password = request.form.get("password")
    #Save session variable
    if session.get("user") is None:
        session["user"] = username
    #user/pass not in db yet
    if db.execute("SELECT * FROM users WHERE username =:username AND password =:password",{"username":username,"password":password}).rowcount==0:
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                {"username":username, "password":password})
        db.commit()
        return render_template("day.html")
    else: #user/pass already in db (old user)
        return render_template("day.html")

@app.route("/<date>", methods = ["GET","POST"])
def day(date):
    # expected input: YYYY-DD-MM
    year, day, month = date.split("-")
    long = db.execute("SELECT ")
    short = db.execute("SELECT")
    
    return render_template("day.html", year=year, day=day, month=month)

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")
