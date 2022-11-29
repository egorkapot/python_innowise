import pytest

from configs.conf_db import Config


@pytest.fixture
def get_config():
    config = Config().get_config()
    return config

