from mongoengine import Document, IntField, StringField


class users(Document):
    """
    User collection stores user information
    """
    username = StringField(max_length=20, required=True, unique=True)
    password = StringField(max_length=20, required=True)
    author_bio = StringField(max_length=20, required=True)
    fav_film = StringField(max_length=20, required=True)
    first_name = StringField(max_length=20, required=True)
    last_name = StringField(max_length=20, required=True)
    profile_img = StringField(max_length=20, required=True, unique=True)


class categories(Document()):
    """
    Category collection, stores category information
    """
    category_name = StringField(max_length=20, required=True, unique=True)
    category_image = StringField(max_length=20, required=True, unique=True)


class reviews(Document):
    """
    Reviews Collection, stores Reviews information
    """
    review_image = StringField(max_length=20, required=True)
    film_name = StringField(max_length=20, required=True)
    review_title = StringField(max_length=20, required=True)
    category_name = StringField(max_length=20, required=True)
    review_description = StringField(max_length=20, required=True)
    created_by = StringField(max_length=20, required=True)
    rating = IntField(max_length=20, required=True)
    publish_date = StringField(max_length=20, required=True)
