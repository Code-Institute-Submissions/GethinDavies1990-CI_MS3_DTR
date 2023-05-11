from binge_reviews import create_app


def test_routes(client):
    """
    This test function tests, the home routes
    """
    response = client.get("/get_reviews")
    assert b"<title>Reviews</title>" in response.data


def test_routes(client):
    """
    This test function tests the add_review function.
    Checks to see if the response data includes the title of 'Add Review'
    It will then add a mock collection of review to the mock database.
    once the mock collection of 'reviews' is created,
    it tests adding a review to the database.
    It then uses the assert method to check the data
    returned matches the data that has been input into the database
    """
    response = client.get("/add_review")
    assert b"<title>Add Review</title>" in response.data


def test_add_review(mongo_database):
    collection_name = 'reviews'
    collection = mongo_database.create_collection(collection_name)

    review = {
        "review_image": "test image",
        "film_name": "Batman",
        "review_title": "Test title",
        "category_name": "test category",
        "review_description": "test description",
        "created_by": "test user",
        "rating": "5",
        "publish_date": "11/05/2023"
    }

    collection.insert_one(review)

    result = collection.find({})
    num_documents = len(list(result))
    assert num_documents == 1, f"Expected 1 document, but found {num_documents}"

    inserted_document = collection.find_one({})
    assert inserted_document["review_image"] == "test image", "Expected review_image to be 'test image'"
    assert inserted_document["film_name"] == "Batman", "Expected film_name to be 'Batman'"
    assert inserted_document["review_title"] == "Test title", "Expected review_title to be 'Test title'"
    assert inserted_document["category_name"] == "test category", "Expected category_name to be 'test category'"
    assert inserted_document["review_description"] == "test description", "Expected review_description to be 'test description'"
    assert inserted_document["created_by"] == "test user", "Expected created_by to be 'test user'"
    assert inserted_document["rating"] == "5", "Expected rating to be '5'"
    assert inserted_document["publish_date"] == "11/05/2023", "Expected publish_date to be '11/05/2023'"


def test_register(mongo_database):
    """
    This test function tests the register function.
    It will then add a mock collection of users to the mock database.
    once the mock collection of 'users' is created,
    it tests adding a user to the database.
    It then uses the assert method to check the data
    returned matches the data that has been input into the database
    """

    collection_name = 'users'
    collection = mongo_database.create_collection(collection_name)

    users = {
        "username": "test123",
        "password": "password123",
        "first_name": "Chad",
        "last_name": "Phillips",
        "fav_film": "Lego",
        "user_img": "chad image"
    }

    collection.insert_one(users)

    result = collection.find({})
    num_documents = len(list(result))
    assert num_documents == 1, f"Expected 1 document, but found {num_documents}"

    inserted_document = collection.find_one({})
    assert inserted_document["username"] == "test123", "Expected username to be 'test123'"
    assert inserted_document["password"] == "password123", "Expected password to be 'password123'"
    assert inserted_document["first_name"] == "Chad", "Expected first_name to be 'Chad'"
    assert inserted_document["last_name"] == "Phillips", "Expected last_name to be 'Phillips'"
    assert inserted_document["fav_film"] == "Lego", "Expected fav_film to be 'lego'"
    assert inserted_document["user_img"] == "chad image", "Expected user_img to be 'chad image'"


def test_login(mongo_database):
    """
    This test function tests the register function.
    It will then add a mock collection of users to the mock database.
    once the mock collection of 'users' is created,
    it tests adding a user to the database.
    It then uses the assert method to check the data
    returned matches the data that has been input into the database
    """

    collection_name = 'users'
    collection = mongo_database.create_collection(collection_name)
    # register users
    users = {
        "username": "test123",
        "password": "password123",
        "first_name": "Chad",
        "last_name": "Phillips",
        "fav_film": "Lego",
        "user_img": "chad image"
    }

    collection.insert_one(users)
    response = client.post("/login", data={"username": "test123", "password": "password123"})
    assert b"<title>Login</title>" in response.data

    inserted_document = collection.find_one({})
    assert inserted_document["username"] == "test123", "Expected username to be 'test123'"
    assert inserted_document["password"] == "password123", "Expected password to be 'password123'"


