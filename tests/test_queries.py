import pytest

@pytest.fixture()
def get_query_dict():
    from utils.queries import Queries, get_query_dict

    return get_query_dict

def test_get_query_dict(get_query_dict):
    assert 


