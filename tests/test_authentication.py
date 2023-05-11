from binge_reviews import create_app


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


# def test_login(mongo_database):
#     """
#     This test function tests the register function.
#     It will then add a mock collection of users to the mock database.
#     once the mock collection of 'users' is created,
#     it tests adding a user to the database.
#     It then uses the assert method to check the data
#     returned matches the data that has been input into the database
#     """

#     collection_name = 'users'
#     collection = mongo_database.find_one(collection_name)
#     # register users
#     users = {
#         "username": "test123",
#         "password": "password123",
#         "first_name": "Chad",
#         "last_name": "Phillips",
#         "fav_film": "Lego",
#         "user_img": "chad image"
#     }

#     collection.insert_one(users)
#     response = client.post("/login", data={"username": "test123", "password": "password123"})
#     assert b"<title>Login</title>" in response.data

#     inserted_document = collection.find_one({})
#     assert inserted_document["username"] == "test123", "Expected username to be 'test123'"
#     assert inserted_document["password"] == "password123", "Expected password to be 'password123'"


