from __future__ import annotations

import pytest

from configs.conf_db import Config


@pytest.fixture()
def connection_string_result():
    return 'postgresql://egor_check:egor_check@127.1.1.1:5444/egor_check'


@pytest.fixture
def right_connection_string():
    config = Config().create_connection()
    return config
