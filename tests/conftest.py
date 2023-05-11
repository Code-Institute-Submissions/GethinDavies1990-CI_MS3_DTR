import pytest
from binge_reviews import create_app
import mongomock


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope='session')
def mongo_client():
    return mongomock.MongoClient()


@pytest.fixture(scope='function')
def mongo_database(mongo_client):
    return mongo_client.db_name
