from binge_reviews import create_app


def test_add_category(mongo_database):
    """
    This function tests the add_category function
    adds a mock category
    assert checks if the mock category was added to the database.
    """
    collection_name = 'categories'
    collection = mongo_database.create_collection(collection_name)

    category = {
        "category_name": "test category",
        "category_image": "category Test",

    }

    collection.insert_one(category)

    result = collection.find({})
    num_documents = len(list(result))
    assert num_documents == 1, f"Expected 1 document, but found {num_documents}"

    inserted_document = collection.find_one({})
    assert inserted_document["category_name"] == "test category", "Expected category_name to be 'test category'"
    assert inserted_document["category_image"] == "category Test", "Expected category_image to be 'category Test'"


def test_update_category(mongo_database):
    """
    This function tests the edit_category function,
    adds a mock category
    updates data
    insert update
    assert method is called to check the collection has been updated.
    """
    collection_name = 'update_categories'
    collection = mongo_database.create_collection(collection_name)

    category = {
        "category_name": "test category",
        "category_image": "category Test",
    }

    collection.insert_one(category)

    new_data = {
        "category_name": "updated category name",
        "category_image": "updated category image",
    }
    collection.update_one({"category_name": "test category"}, {"$set": new_data})

    updated_document = collection.find_one({"category_name": "updated category name"})
    assert updated_document is not None, "Expected to find an updated document"
    assert updated_document["category_image"] == "updated category image", "Expected category_image to be 'updated category image'"

