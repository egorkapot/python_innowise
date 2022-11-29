import pytest

from modules.postgresdb import Postgres


@pytest.fixture
def write_dataframe_to_database():
    Postgres().write_dataframe_to_database()
