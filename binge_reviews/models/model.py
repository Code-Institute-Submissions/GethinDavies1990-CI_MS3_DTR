from mongoengine import Document, IntField, StringField


class users(Document):
    """
    User collection stores usr information
    """
    username = StringField(max_length=20, required=True, unique=True)
    password = StringField(max_length=20, required=True)
    author_bio = StringField(max_length=20, required=True)
    fav_film = StringField(max_length=20, required=True)
    first_name = StringField(max_length=20, required=True)
    last_name = StringField(max_length=20, required=True)
    profile_img = StringField(max_length=20, required=True, unique=True)


class users(Categories):
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
