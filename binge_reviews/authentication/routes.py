from flask import (Flask, flash,
                   render_template, redirect,
                   request, session, url_for, Blueprint)
from werkzeug.security import generate_password_hash, check_password_hash
from binge_reviews import mongo
from bson.objectid import ObjectId
from binge_reviews.util import util


# Create authentication object as a blueprint
authentication = Blueprint('authentication', __name__)


@authentication.route("/register", methods=["GET", "POST"])
def register() -> object:
    """
    This function registers new users to the website and
    if succesfull on registration will be redirected to their
    profile page. The users password is encrypted. If the
    username already exists they are redirected back
    to the register page, and will be prompted with an alert
    to make them aware it is already in use.
    :return render_template of profile.html
    """
    if request.method == "POST":
        image_url = util.upload_image('user_img')
        # check if username already exsists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        #  If user already exists, redirects them to register page
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("authentication.register"))
        register = {
            "user_img": image_url,
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "fav_film": request.form.get("fav_film"),
            "author_bio": request.form.get("author_bio")
        }
        try:
            # Insert the user in to the register object
            mongo.db.users.insert_one(register)
            # put user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful")
        except Exception as e:
            flash("An excpetion has occurred when adding new user: " +
                  getattr(e, 'message', repr(e)))
        return redirect(
            url_for("authentication.profile", username=session["user"]))
    return render_template("authentication/register.html")


@authentication.route('/login', methods=['GET', "POST"])
def login() -> object:
    """
    This function will login the user if they use a matched
    username and password. The user is redirected to their profile page.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "authentication.profile", username=session["user"]))
            else:
                #  invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("authentication.login"))
        else:
            #  username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("authentication.login"))

    return render_template("authentication/login.html")


@ authentication.route("/logout")
def logout():
    """
    This function logs the user out of their
    session and will be redirected to the login page.
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("authentication.login"))


@authentication.route("/profile/<username>", methods=["GET", "POST"])
def profile(username: object) -> object:
    """
    This function will render the profile page of the logged in user
    and display their profile information.
    :param username: username of user
    :return render_template of profile.html
    """
    # if user not logged in, redirect to login page
    if 'user' not in session:
        return redirect(url_for("authentication.login"))
    # grab session user's username from db
    user = mongo.db.users.find_one(
        {"username": username})
    reviews = list(mongo.db.reviews.find())

    if session["user"]:
        return render_template(
            "authentication/profile.html", username=session['user'],
            user=user, reviews=reviews)

    return redirect(url_for("authentication.login"))


@authentication.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    """
    This function updates users profile with updated information
    they have submitted
    :param username: username of the user
    :return: a redirect to the updated profile page or 
    a template for updating profile
    """
    # Create an object update_profile with updated information
    if request.method == "POST":
        # Get the user
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        #  Create an object update_profile with updated information
        update_profile = {"$set": {
            "username": session['user'],
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "fav_film": request.form.get("fav_film"),
        }}
        try:
            # Update the user information in the users collection
            mongo.db.users.update_one({"username": username}, update_profile)
            flash("Profile Successfully Updated")
        except Exception as e:
            flash("An exception occured when adding user: " +
                  getattr(e, 'message', repr(e)))
        # Find user and redirect them to their updated profile page
        user = mongo.db.users.find_one({"username": username})
        return redirect(url_for('authentication.profile', username=username))
    else:
        # Get the user object
        user = mongo.db.users.find_one({"username": username})
        return render_template("authentication/update-profile.html",
                               username=session['user'], user=user)


@authentication.route("/delete_profile/<username>")
def delete_profile(username: object) -> object:
    """
    This function deletes the profile of the user
    :param username: username of the user
    :return redirect to homepage
    """
    try:
        # Delete users collection from db
        mongo.db.users.delete_one({"username": username})
        # redirects user to the homepage
        flash("Your account has been deleted and you have been logged out")
        session.pop("user")
    except Exception as e:
        flash("An exception occured when delting user: " +
              getattr(e, 'message'), repr(e))
    return redirect(url_for("reviews.get_reviews"))
