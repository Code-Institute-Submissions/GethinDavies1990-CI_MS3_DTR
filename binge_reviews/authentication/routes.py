from flask import (Flask, flash,
                   render_template, redirect,
                   request, session, url_for, Blueprint)
from werkzeug.security import generate_password_hash, check_password_hash
from binge_reviews import mongo

# Create authentication object as a blueprint
authentication = Blueprint('authentication', __name__)


@authentication.route("/register", methods=["GET", "POST"])
def register():
    """
    This function registers new users to the website and
    if succesfull on registration will be redirected to their
    profile page. The users password is encrypted. If the
    username already exists they are redirected back
    to the register page, and will be promted with an alert
    to make them aware it is already in use.
    """
    if request.method == "POST":
        # check if username already exsists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("authentication.register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "fav_film": request.form.get("fav_film")
        }
        mongo.db.users.insert_one(register)

        # put user into 'session' cokkie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(
            url_for("authentication.profile", username=session["user"]))
    return render_template("register.html")


@authentication.route('/login', methods=['GET', "POST"])
def login():
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

    return render_template("login.html")


@authentication.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    This function will render the profile page of the logged in user
    and display their profile information.
    """
    # grab session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("authentication.login"))


@authentication.route("/logout")
def logout():
    """
    This function logs the user out of their
    session and will be redirected to the login page.
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("authentication.login"))
