import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Page Displays
@app.route("/")
def index():
    """ Displays home page """
    return render_template("index.html")


# displays recipe page
@app.route("/get_recipes")
def get_recipes():
    """ Gets the recipes data from database and displays it on the pag e"""
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/get_about")
def get_about():
    """ Displays About page """
    return render_template("about.html")


@app.route("/get_contact")
def get_contact():
    """ Displays Contact page """
    return render_template("contact.html")


@app.route("/get_login")
def get_login():
    """ Displays login page """
    return render_template("login.html")


@app.route("/get_signup", methods=["GET", "POST"])
def get_signup():
    """ Displays sign up page """
    return render_template("signup.html")

@app.route("/get_profile")
def get_profile():
    """ Displays profile page """
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
