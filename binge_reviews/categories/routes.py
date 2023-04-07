from flask import (Flask, flash,
                   render_template, redirect,
                   request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from binge_reviews import mongo


# Create a reviews object as a blueprint
categories = Blueprint('categories', __name__)


@categories.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@categories.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for('get_categories'))

    return render_template("add_category.html")


@categories.route("/edit_category/<category_id>", methods=["POST", "GET"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {"$set": {
            "category_name": request.form.get("category_name")
        }}
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for('get_categories'))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@categories.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))
