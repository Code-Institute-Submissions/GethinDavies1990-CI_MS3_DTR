from flask import (Flask, flash,
                   render_template, redirect,
                   request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from binge_reviews import mongo
from binge_reviews.util import util


# Create a reviews object as a blueprint
categories = Blueprint('categories', __name__)


@categories.route("/get_categories")
def get_categories():
    """
    This function will display all the categories
    in a grid section on the page
    """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories/categories.html", categories=categories)


@categories.route("/add_category", methods=["GET", "POST"])
def add_category() -> object:
    """
    This function lets the user add new catagories and images to the
    application.
    """
    if request.method == "POST":
        image_url = util.upload_image('category_image')
        category = {
            "category_image": image_url,
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for('categories.get_categories'))

    return render_template("categories/add_category.html")


@categories.route("/edit_category/<category_id>", methods=["POST", "GET"])
def edit_category(category_id):
    """
    This function will allow the admin user
    to edit a category name and image.
    """
    if request.method == "POST":
        image_url = util.upload_image('category_image')
        submit = {"$set": {
            "category_image": image_url,
            "category_name": request.form.get("category_name")
        }}
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for('categories.get_categories'))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("categories/edit_category.html", category=category)


@categories.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    This function allows the admin user to delete
    categories.
    """
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("categories.get_categories"))
