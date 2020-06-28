import os

import datetime
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

#Home page (fill in users database)
@app.route("/", methods=["GET","POST"])
def index():
    users = db.execute("SELECT * FROM users").fetchall()
    return render_template("index.html", users = users)

#Login route
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    #Save session variable
    if session.get("user") is None:
        session["user"] = username
    #user/pass not in db yet (new user)
    if db.execute("SELECT * FROM users WHERE username =:username AND password =:password",{"username":username,"password":password}).rowcount==0:
        if db.execute("SELECT * FROM users WHERE username =:username", {"username":username}).rowcount>0:
            return render_template("error.html", message="User already exists.")
        else:
            db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                    {"username":username, "password":password})
            db.commit()
        return render_template("choice.html")
    else: #user/pass already in db (old user)
        return render_template("choice.html")


@app.route("/day", methods=["GET","POST"])
def day():
    #User selects how much time to spend 
    if request.method == "POST":
        time_selected = request.form.get("time_selected")
        #select 1 resource whose length matches time selected by user (short/med/long)
        resource = db.execute("SELECT * FROM resources WHERE length = :length", {"length":time_selected}).fetchone()
        if resource is None:
            return render_template("error.html", message="Couldn't find a resource")
    #get today's date 
    today = datetime.datetime.now()
    today = today.strftime("%Y-%m-%d")
    year, day, month = today.split("-")
    #show chosen resource
    return render_template("day.html", resource=resource, year=year, day=day, month=month )

#Shows month calendar 
@app.route("/calendar", methods=["GET","POST"])
def calendar():
    return render_template("calendar.html")