from binge_reviews.util import util


def test_get_timestamp():
    """
    This test asserts the timestamp is in the
    correct format and length
    """
    timestamp = util.get_timestamp()
    assert (timestamp.endswith("2023"))
