from __future__ import annotations

import pytest

from configs.conf_db import Config
from modules.etl import ETL
from utils.queries import Queries


@pytest.fixture()
def connection_string_result():
    return 'postgresql://test:test@db:5432/test'


@pytest.fixture
def right_connection_string():
    return Config().create_connection()


@pytest.fixture
def get_test_dict():
    return {
        'query_1': 'SELECT 1 FROM check',
        'query_2': 'SELECT 2 FROM check',
        'schema': """CREATE SCHEMA IF NOT EXISTS test;
CREATE TABLE IF NOT EXISTS test.rooms (
id int PRIMARY KEY,
name VARCHAR(50));
CREATE TABLE IF NOT EXISTS test.students (
birthday DATE,
id int,
name VARCHAR(60),
room int,
sex CHAR(1),
FOREIGN KEY (room) REFERENCES test.rooms(id) ON DELETE CASCADE);""",
    }


@pytest.fixture
def create_class_queries():
    return Queries(directory='tests/fixtures/test_queries/')


@pytest.fixture
def pg_conn_string():
    return 'postgresql://test:test@172.17.0.2:5432/test'


@pytest.fixture
def etl_object(mocker, pg_conn_string):

    def my_init(self, directory='tests/fixtures/test_queries'):
        self.directory = directory
        self.query_dict = self._load_queries()

    mocker.patch('utils.queries.Queries.__init__', my_init)

    # Replace the `Config.create_connection` method with a mock that returns the mock config
    mocker.patch.object(Config, 'create_connection', return_value=pg_conn_string)

    etl = ETL()
    etl.ROOMS = 'tests/fixtures/test_etl/test_rooms.json'
    etl.STUDENTS = 'tests/fixtures/test_etl/test_students.json'
    print(etl.queries)
    # Create an instance of the ETL class
    return etl
