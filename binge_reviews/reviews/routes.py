from flask import (Flask, flash,
                   render_template, redirect,
                   request, session, url_for, Blueprint)
from bson.objectid import ObjectId
from binge_reviews import mongo
from binge_reviews.util import util


# Create a reviews object as a blueprint
reviews = Blueprint('reviews', __name__)


@reviews.route("/")
@reviews.route("/get_reviews")
def get_reviews():
    """
    This function will display all the reviews posted
    by users.
    """
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews/reviews.html", reviews=reviews)


@reviews.route("/get_review/<review_id>",)
def get_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    return render_template("reviews/review.html", review=review)


@reviews.route("/search", methods=["GET", "POST"])
def search():
    """
    This function allows the user to search for reviews by
    film name and by review description.
    """
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews/reviews.html", reviews=reviews)


@reviews.route("/add_review", methods=["GET", "POST"])
def add_review() -> object:
    """
    This function allows the user to add reviews to the
    application. On succesfull submission the user is
    redirected to the reviews.html page.
    """

    if request.method == "POST":
        try:
            # Store Review image in S3 Bucket
            image_url = util.upload_image('review_image')
            # Generate timestamp
            timestamp = util.get_timestamp()
            review = {
                "review_image": image_url,
                "film_name": request.form.get("film_name"),
                "review_title": request.form.get("review_title"),
                "category_name": request.form.get("category_name"),
                "review_description": request.form.get("review_description"),
                "created_by": session["user"],
                "rating": request.form.get("rating"),
                "publish_date": timestamp
            }
            mongo.db.reviews.insert_one(review)
            flash("Review Published")
        except Exception as e:
            flash("An exception occured when adding user: " +
                  getattr(e, 'message', repr(e)))
        return redirect(url_for('reviews.get_reviews'))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("reviews/add_review.html", categories=categories)


@reviews.route("/edit_review/<review_id>", methods=["POST", "GET"])
def edit_review(review_id):
    """
    This function allows the user to edit their own
    review, the user must be in session and can only edit their
    own reviews.
    """
    if request.method == "POST":
        try:
            submit = {"$set": {
                "film_name": request.form.get("film_name"),
                "review_title": request.form.get("review_title"),
                "category_name": request.form.get("category_name"),
                "review_description": request.form.get("review_description"),
                "created_by": session["user"],
                "rating": request.form.get("rating")
            }}
            mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, submit)
            flash("Review Successfully Edited")
        except Exception as e:
            flash("An exception occured when adding user: " +
                  getattr(e, 'message', repr(e)))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "reviews/edit_review.html", review=review, categories=categories)


@reviews.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    This function allows the user to delete their own reviews.
    they will not be able to delete other user reviews.
    """
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Review Successfully Removed")
    return redirect(url_for('reviews.get_reviews'))
