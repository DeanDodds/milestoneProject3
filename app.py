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


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Displays login page """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if the username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """ Displays sign up page and checks user inputs"""
    if request.method == "POST":
        # checks if user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup.html"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

    # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign up successfull!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """"displays profile page"""""
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    #gets recipes from database
    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template("profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ remove user from session cookie """
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("login"))


@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    """"get recipe catergoies and cusine from database and displays addrecipe page"""
    if request.method == "POST":
        recipe = {
            "author": session["user"],
            "catergory_name": request.form.get("catergory_name"),
            "cusine_name": request.form.get("cusine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": request.form.get("servings"),
            "instructions": request.form.get("instructions"),
            "img_url": request.form.get("img_url"),
            "description": request.form.get("description")
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Task Successfully Added")
        return redirect(url_for("profile", username=session["user"]))
        
    cuisine = mongo.db.cuisine.find().sort("cuisine_name, 1")
    catergories = mongo.db.catergories.find().sort("catergory_name, 1")
    return render_template("addrecipe.html", cuisine=cuisine, catergories=catergories)


@app.route("/editrecipe/<recipe_id>", methods=["GET", "POST"])
def editrecipe(recipe_id):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    catergories = mongo.db.catergories.find().sort("catergory_name, 1")
    cuisine = mongo.db.cuisine.find().sort("cuisine_name, 1")
    return render_template("editrecipe.html", cuisine=cuisine, catergories=catergories, recipe=recipe)

@app.route("/favourites")
def favourites():
    """ Display favourites page """
    return render_template("favourites.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
