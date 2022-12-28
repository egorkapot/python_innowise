from __future__ import annotations

import pytest

from utils.queries import Queries


def test_can_create_dict(create_class_queries):
    expected_result = create_class_queries.query_dict
    assert isinstance(expected_result, dict)


def test_values_in_dict(get_test_dict, create_class_queries):
    result = create_class_queries.query_dict
    print(get_test_dict)
    assert get_test_dict == result


def test_can_not_create_dict_directory_is_incorrect():
    with pytest.raises(FileNotFoundError):
        Queries(directory='somedirectory')
