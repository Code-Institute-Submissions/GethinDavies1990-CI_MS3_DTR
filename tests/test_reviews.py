from binge_reviews import create_app


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


def test_update_review(mongo_database):
    """
    This function tests the edit_category function,
    adds a mock category
    updates data
    insert update
    assert method is called to check the collection has been updated.
    """
    collection_name = 'update_review'
    collection = mongo_database.create_collection(collection_name)

    review = {
        "review_image": "image",
        "film_name": "Superman",
        "review_title": "Title",
        "category_name": "Category",
        "review_description": "description",
        "created_by": "user",
        "rating": "3",
        "publish_date": "12/05/2023"
    }

    collection.insert_one(review)

    update_review = {
        "review_image": "image",
        "film_name": "Batman",
        "review_title": "Title",
        "category_name": "Category",
        "review_description": "description",
        "created_by": "user",
        "rating": "3",
        "publish_date": "12/05/2023"
    }
    collection.update_one({"film_name": "Superman"}, {"$set": update_review})

    updated_document = collection.find_one({"film_name": "Batman"})
    assert updated_document is not None, "Expected to find an updated document"
    assert {k: v for k, v in updated_document.items() if k != '_id'} == update_review, "Expected document to match updated_review dictionary"


