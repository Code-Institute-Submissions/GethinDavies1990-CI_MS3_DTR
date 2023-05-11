from binge_reviews import create_app


def test_routes(client):
    """
    This test function tests, the home routes
    """
    response = client.get("/get_reviews")
    assert b"<title>Reviews</title>" in response.data
