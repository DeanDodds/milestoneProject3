import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, )
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
    """ Displays Main Recipe page """
    # Gets recipes from the database
    recipes = mongo.db.recipes.find()
    # Checks if user is logged
    if "user" in session:
        # Gets the users favourites from the database 
        favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
        # Gets the users the users id from the databas
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        return render_template(
            "recipes.html", user_id=user_id,
            recipes=recipes, favourites=favourites)
    return render_template("recipes.html", recipes=recipes,)


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
        # Checks if user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Checks if the user name is already in the databse 
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup.html"))
        # Store user information in to a variable
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourites": [],
        }
        # inserts user info into the database
        mongo.db.users.insert_one(register)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # confirmation message for the user 
        flash("Sign up successfull!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """"displays profile page"""""
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # gets recipes from database
    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ remove user from session cookie """
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("login"))


@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    """"get recipe catergoies and cusine
    from database and displays addrecipe page"""
    if request.method == "POST":
        recipe = {
            "author": session["user"],
            "catergory_name": request.form.get("catergory_name"),
            "cusine_name": request.form.get("cusine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": request.form.get("servings"),
            "instructions": request.form.get("instructions"),
            "img_url": request.form.get("img_url"),
            "description": request.form.get("description"),
            "rating": [],
            "star_ratings": []
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Task Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    cuisine = mongo.db.cuisine.find().sort("cuisine_name, 1")
    catergories = mongo.db.catergories.find().sort("catergory_name, 1")
    return render_template(
        "addrecipe.html", cuisine=cuisine, catergories=catergories)


@app.route("/editrecipe/<recipe_id>", methods=["GET", "POST"])
def editrecipe(recipe_id):
    if request.method == "POST":
        submit = {
            "author": session["user"],
            "catergory_name": request.form.get("catergory_name"),
            "cusine_name": request.form.get("cusine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": request.form.get("servings"),
            "instructions": request.form.get("instructions"),
            "img_url": request.form.get("img_url"),
            "description": request.form.get("description")
        }
        mongo.db.recipes.replace_one(
                    {"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    catergories = mongo.db.catergories.find().sort("catergory_name, 1")
    cuisine = mongo.db.cuisine.find().sort("cuisine_name, 1")
    return render_template(
        "editrecipe.html", 
        cuisine=cuisine, catergories=catergories, recipe=recipe)


@app.route("/add_recipe_rating/<recipe_id>", methods=["GET", "POST"])
def add_recipe_rating(recipe_id):
    """ Add recipe star rating to the star ratings field 
    and then works out he average. Then updates the rating feild"""
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    if request.method == "POST":
        # Gets the new rating from form
        new_rating = request.form.get('star_ratings')  
        # Inserts the new star rating into 
        # the star ratings field as an interger  
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, 
            {"$addToSet": {"star_ratings": int(new_rating)}})
        # Gets the new array of ratings and find the average
        ratings = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})["star_ratings"]
        # Find the average
        sum_of_ratings = 0
        for rating in ratings:
            sum_of_ratings = sum_of_ratings + rating
        average_rating = sum_of_ratings / len(ratings)
        # Addnew rating to the database 
        
        # Display confirmation message to the user     
        flash("thanks or the rating")

    return render_template(
        "recipepage.html", recipe=recipe, recipe_id=recipe_id)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """Delete recipe from databse"""
    mongo.db.recipes.delete_one()
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/add_favourites/<recipe_id>")
def add_favourites(recipe_id):

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]

    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)}, 
        {"$addToSet": {"favourites": ObjectId(recipe_id)}})
    flash("Recipe saved to favourites!")

    # gets recipes from database
    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes,
            user_id=user_id, favourites=favourites, recipe_id=recipe_id)


@app.route("/favourites/)")
def favourites():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    favourites = mongo.db.users.find_one(
        {"username": session["user"]})["favourites"]
    recipes = mongo.db.recipes.find()
    
    return render_template(
        "favourites.html", user_id=user_id,
        username=username,  favourites=favourites, recipes=recipes)


@app.route("/remove_from_favourites/<recipe_id>")
def remove_from_favourites(recipe_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    favourites = mongo.db.users.find_one(
        {"username": session["user"]})["favourites"]
    recipes = mongo.db.recipes.find()
    flash("recipe removed from favourites")

    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)}, 
        {"$pull": {"favourites": ObjectId(recipe_id)}})
    return render_template(
        "favourites.html", user_id=user_id,
        username=username, favourites=favourites, recipes=recipes)


@app.route("/recipe_page/<recipe_id>")
def recipe_page(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template(
        "recipepage.html", recipe=recipe, recipe_id=recipe_id)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
