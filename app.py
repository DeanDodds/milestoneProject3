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
    recipes = list(mongo.db.recipes.find())
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
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                # Gets username from form
                session["user"] = request.form.get("username").lower()
                # Display confirmation to the user
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
            flash("Username already exists. Please choose another username")
            return redirect(url_for("signup"))
        # Store user information in to a variable
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourites": [],
            "admin": "off"
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
    # checks if user is in session
    if 'user' in session:
        # get the session user's username from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        check_admin = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
        # gets recipes from database
        recipes = list(mongo.db.recipes.find())
        # gets user favourites from the database
        favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
        if check_admin == "on":
            return render_template(
                "profile.html", username=username,
                recipes=recipes, favourites=favourites, admin=check_admin)
        else:
            return render_template(
                "profile.html", username=username,
                recipes=recipes, favourites=favourites)
    # Message for the user
    flash('Please log in to view profile')
    return redirect(url_for("login"))


@app.route("/control")
def control():
    if 'user' in session:
        """ Dispalys control panel for admin users """
        username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        check_admin = mongo.db.users.find_one(
                {"username": session["user"]})["admin"]
        recipes = list(mongo.db.recipes.find())
        users = list(mongo.db.users.find())
        if check_admin == "on":
            return render_template("control.html", 
                                   recipes=recipes, 
                                   users=users, admin=check_admin)
        else:
            favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
            flash('Please log on to an admin account to view this page')
            return redirect(url_for("profile",username=username,
                recipes=recipes, favourites=favourites))

    flash('You must be logged in to view this page')
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ remove user from session cookie """
    # Removes session user
    session.pop("user")
    # Comfirmation message to user
    flash("You have been logged out")
    return redirect(url_for("login"))


@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    """"get recipe catergoies and cusine
    from database and displays addrecipe page"""
    if 'user' in session:
        if request.method == "POST":
            # Get the data from the add recipe form
            recipe = {
                "author": session["user"],
                "catergory_name": request.form.get("catergory_name"),
                "cuisine_name": request.form.get("cuisine_name"),
                "recipe_name": request.form.get("recipe_name"),
                "servings": request.form.get("servings"),
                "instructions": request.form.get("instructions").splitlines(),
                "img_url": request.form.get("img_url"),
                "description": request.form.get("description"),
                "ingredients": request.form.get("ingredients").splitlines(),
                "rating": (3),
                "star_ratings": [3]
            }
            # Inserts data into the recipe database
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe Successfully Added")
            return redirect(url_for("profile", username=session["user"]))
        # Gets the catergorie names from database
        catergories = mongo.db.catergories.find().sort("catergory_name, 1")
        # Gets the cuisine names from database
        cuisines = list(mongo.db.cuisines.find().sort("cuisine_name, 1"))
        print(catergories)
        print(cuisines)
        return render_template(
            "addrecipe.html", catergories=catergories, cuisines=cuisines)
    # Displays a message to user
    flash('Please log in to add a recipe')
    return redirect(url_for("login"))


@app.route("/editrecipe/<recipe_id>", methods=["GET", "POST"])
def editrecipe(recipe_id):
    """ Displays edit recipe form """
    # Gets recipe from in the database to edit
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Gets the catergouries from the database
    catergories = list(mongo.db.catergories.find().sort("catergory_name, 1"))
    # Gets the cuisine names from the database
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name, 1"))
    # Gets Favourites ffrom  the database
    favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
    # Gets username from database
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    check_admin = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
    # Gets name from database
    author = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})["author"]
    if request.method == "POST":
        # Gets the current star ratings from the database
        star_ratings = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})["star_ratings"]
        # Gets the current star ratings from the database
        rating = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})["rating"]
        # Get the data from form and saves it as a variable
        submit = {
            "author": session["user"],
            "catergory_name": request.form.get("catergory_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": request.form.get("servings"),
            "instructions": request.form.get("instructions").splitlines(),
            "img_url": request.form.get("img_url"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients").splitlines(),
            "rating": rating,
            "star_ratings": star_ratings
        }
        if author == username or check_admin == "on":
            mongo.db.recipes.replace_one(
                    {"_id": ObjectId(recipe_id)}, submit)
            # Gets updated recipes from the database
            recipes = list(mongo.db.recipes.find())
            # Displays Confoirmation message
            flash("recipe sucessfully updated")
            return render_template(
                "profile.html", username=username,
                recipes=recipes, favourites=favourites)
    if 'user' in session:
        return render_template("editrecipe.html",
                               cuisines=cuisines, catergories=catergories,
                               recipe=recipe)
    # If users not logged im they get redirected to log in
    flash('Please log in to edit recipe')
    return redirect(url_for("login"))


@app.route("/add_recipe_rating/<recipe_id>", methods=["GET", "POST"])
def add_recipe_rating(recipe_id):
    """ Add recipe star rating to the star ratings field
    and then works out he average. Then updates the rating feild"""
    # checks if the user is logged in
    print("rating")
    if "user" in session:
        print("in session")
        if request.method == "POST":
            print('post')
            # Gets the new rating from form
            new_rating = request.form.get('star_ratings')
            # Inserts the new star rating into the star ratings array
            mongo.db.recipes.update_one(
                {"_id": ObjectId(recipe_id)},
                {"$push": {"star_ratings": int(new_rating)}})
            # Gets the new array of ratings and find the average
            ratings = mongo.db.recipes.find_one(
                {"_id": ObjectId(recipe_id)})["star_ratings"]
            # get the average star rating of the ratings array
            sum_of_ratings = 0
            for rating in ratings:
                sum_of_ratings = sum_of_ratings + rating
            average_rating = sum_of_ratings / len(ratings)
            # round off  average user rating to 2 decimal places
            average_rating = "{:.2f}".format(average_rating)
            # Addnew rating to the database
            mongo.db.recipes.update_one(
                {"_id": ObjectId(recipe_id)},
                {"$set": {"rating": float(average_rating)}})
            # Display confirmation message to the user
            flash("thanks or the rating")
            # gets recipes from the database
            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template("recipepage.html",
                               recipe=recipe, recipe_id=recipe_id)
    # If users not logged in redirects them to login page
    flash('Please log in to rate a recipe')
    return redirect(url_for("login"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """Delete recipe from database"""
    # Check if user in session
    if 'user' in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        author = mongo.db.recipes.find_one(
                {"_id": ObjectId(recipe_id)})["author"]
        check_admin = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
        if username == author or check_admin == "on":
            # Deletes the document from the database
            mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
            flash("Recipe Successfully Deleted")
            return redirect(url_for("get_recipes"))
        else:
            flash("You can only delete recipes you have created")
            return redirect(url_for("get_recipes"))
    flash('Please log in to rate a recipe')
    return redirect(url_for("login"))


@app.route("/favourites/)")
def favourites():
    """"Displays the users saved recipes on the favourites page"""
    # if user is logged in
    if 'user' in session:
        # Gets the user form database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # Gets the user id form database
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        # Gets Favourites ffrom the database
        favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
        # Gets the recipes from database
        recipes = list(mongo.db.recipes.find())
        return render_template(
            "favourites.html", user_id=user_id,
            username=username,  favourites=favourites, recipes=recipes)
    # If users not logged in redirects them to login page
    flash('Please log in to view your favourites a recipe')
    return redirect(url_for("login"))


@app.route("/add_favourites/<recipe_id>/<page>")
def add_favourites(recipe_id, page):
    """ add favourites to favourites page"""
    if "user" in session:
        # Gets the user form database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # Gets the user id form database
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        # adds the recipe id to the favourites array
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$addToSet": {"favourites": ObjectId(recipe_id)}})
        # User comfirmation message
        flash("Recipe saved to favourites!")
        # gets recipes from database
        recipes = list(mongo.db.recipes.find())

        favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
        # if user signed in
        if page == "recipe_page":
            return render_template(
                "recipes.html", user_id=user_id,
                username=username, favourites=favourites, recipes=recipes)
        elif page == "favourites_page":
            return render_template(
                "favourites.html", user_id=user_id,
                username=username, favourites=favourites, recipes=recipes)
        else:
            return render_template(
                "profile.html", user_id=user_id,
                username=username, favourites=favourites, recipes=recipes)

    # If users not logged in redirects them to login page
    flash('Please log in to edit your favourites a recipe')
    return redirect(url_for("login"))


@app.route("/remove_from_favourites/<recipe_id>/<page>")
def remove_from_favourites(recipe_id, page):
    """removes saved recipes from favourites page"""
    if "user" in session:
        # Gets the user form database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # Gets the user id form database
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        # Removes recipe id from the favourites array
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$pull": {"favourites": ObjectId(recipe_id)}})
        # gets users new favorites from the database
        favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
        # Gets recipes from the database
        recipes = list(mongo.db.recipes.find())
        flash("recipe removed from favourites")
        if page == "recipe_page":
            return render_template(
                "recipes.html", user_id=user_id,
                username=username, favourites=favourites, recipes=recipes)
        elif page == "favourites_page":
            return render_template(
                "favourites.html", user_id=user_id,
                username=username, favourites=favourites, recipes=recipes)
        else:
            return render_template(
                "profile.html", user_id=user_id,
                username=username, favourites=favourites, recipes=recipes)
    flash('Please login to edit your favourites')
    return redirect(url_for("login"))


@app.route("/recipe_page/<recipe_id>")
def recipe_page(recipe_id):
    """Display indivdaul recipe page """
    # Gets the recipe from database with the recipe id
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template(
        "recipepage.html", recipe=recipe, recipe_id=recipe_id)


@app.route("/search/<page>", methods=["GET", "POST"])
def search(page):
    """ Searches for keywords entered by user and returns the results """
    # Gets the users query from the database
    query = request.form.get("query")
    # Searches the database for the users query
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    # Gets the users favourites from the database
    favourites = mongo.db.users.find_one(
            {"username": session["user"]})["favourites"]
    # Gets the user from the database
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    # Gets the users the users id from the databas
    user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
    print(page)
    if page == "recipe_page":
        return render_template(
                "recipes.html", user_id=user_id,
                username=username, favourites=favourites, recipes=recipes)
    elif page == "favourites_page":
        return render_template("favourites.html", user_id=user_id,
                               username=username, favourites=favourites,
                               recipes=recipes)
    else:
        return render_template("profile.html", user_id=user_id,
                               username=username, favourites=favourites,
                               recipes=recipes)


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    """ Deletes user accounts from the database  """
    # Checks if the user is in session
    if "user" in session:
        # Finds the user in the database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        # Checks if the user as admin privaliges
        check_admin = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
        # Checks if the user is logged in the to the account or is admin
        if username == user_id or check_admin == "on":
            recipes = list(mongo.db.recipes.find())
            # Deletes the document from the database
            mongo.db.users.delete_one({"_id": ObjectId(user_id)})
            users = list(mongo.db.users.find())
            # Conformation message to the user
            flash("user Successfully Deleted")
            return render_template("control.html",
                                   recipes=recipes, users=users)
    flash('Please log in to edit your account')
    return redirect(url_for("login"))


@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    """ Edits usernames and admin """
    if "user" in session:
        if request.method == "POST":
            flash("edit")
            user = request.form.get("username")
            admin = request.form.get("admin")
            username = mongo.db.users.find_one(
                {"username": session["user"]})["_id"]
            check_admin = mongo.db.users.find_one(
                {"username": session["user"]})["admin"]
            if username == user_id or check_admin == "on":
                mongo.db.users.update_one(
                    {"_id": ObjectId(user_id)},
                    {"$set": {"username": user}})
                mongo.db.users.update_one(
                    {"_id": ObjectId(user_id)},
                    {"$set": {"admin": admin}})

                recipes = list(mongo.db.recipes.find())
                users = list(mongo.db.users.find())
                flash("User Successfully Updated")
                return render_template("control.html",
                                       recipes=recipes, users=users)
    flash('Please log in to edit your account')
    return redirect(url_for("login"))


@app.route("/subscribe/", methods=["GET", "POST"])
def subscribe():
    """ Adds users who subscribe to the newsletter to the database  """
    if request.method == "POST":
        # Check if email is already in the database
        mailing_list = mongo.db.subscribers.find_one(
            {"email": request.form.get("subscribers")})

        if mailing_list:
            flash("You are already on our mailing list!")
            return ('', 204)

        # Add new email to db
        else:
            subscribe = {
                         "email": request.form.get("subscribers").lower()
                        }

            mongo.db.subscribers.insert_one(subscribe)

            flash("You have successfully subscribed!")
            return ('', 204)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
