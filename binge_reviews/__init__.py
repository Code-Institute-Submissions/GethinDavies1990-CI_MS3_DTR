import os
from flask import Flask
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

# App variables for set up and mongodb connection
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def create_app():
    """
    Create an app with administration, errors, reviews,
    categories blueprint routes
    """
    # Import routes
    # from binge_reviews.administration.routes import administration
    from binge_reviews.authentication.routes import authentication
    from binge_reviews.categories.routes import categories
    # from binge_reviews.errors.routes import errors
    from binge_reviews.reviews.routes import reviews
    # Register routes with app
    # app.register_blueprint(administration)
    app.register_blueprint(authentication)
    app.register_blueprint(categories)
    # app.register_blueprint(errors)
    app.register_blueprint(reviews)
    # return app
    return app
