import pytest

from configs.conf_db import Config
from modules.postgresdb import Postgres


@pytest.fixture
def get_config():
    config = Config().get_config()
    return config



def test_get_config(get_config):
    assert get_config  == 'postgresql://postgres:1@127.0.0.1:5432/task1'



