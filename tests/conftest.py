from __future__ import annotations

import pytest

from configs.conf_db import Config
from utils.queries import Queries


@pytest.fixture()
def connection_string_result():
    return 'postgresql://egor_check:egor_check@127.1.1.1:5444/egor_check'


@pytest.fixture
def right_connection_string():
    config = Config().create_connection()
    return config


@pytest.fixture
def get_test_dict():
    return {'query_1': 'SELECT 1 FROM check', 'query_2': 'SELECT 2 FROM check'}


@pytest.fixture
def create_class_queries():
    return Queries(directory='tests/queries_for_test/')
