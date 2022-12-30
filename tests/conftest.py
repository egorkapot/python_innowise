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
        'query_1': """SELECT s2.room, AGE(s2.max_date, s2.min_date) as age_diff
FROM(
SELECT room, MAX(birthday) OVER(PARTITION BY room) as max_date,
MIN(birthday) OVER(PARTITION BY room) as min_date
FROM task_1.students)s2
GROUP BY s2.room, AGE(s2.max_date, s2.min_date)
ORDER BY age_diff DESC
LIMIT 5""",
        'query_2': """SELECT r.name as room, DATE_TRUNC('day', AVG(AGE(s.birthday))) AS average_age
FROM task_1.students s
JOIN task_1.rooms r
ON s.room = r.id
GROUP BY r.name
ORDER BY average_age
LIMIT 5""",
        'schema': """CREATE SCHEMA IF NOT EXISTS task_1;
CREATE TABLE IF NOT EXISTS task_1.rooms (
id int PRIMARY KEY,
name VARCHAR(50));
CREATE TABLE IF NOT EXISTS task_1.students (
birthday DATE,
id int,
name VARCHAR(60),
room int,
sex CHAR(1),
FOREIGN KEY (room) REFERENCES task_1.rooms(id) ON DELETE CASCADE);""",
    }


@pytest.fixture
def create_class_queries():
    return Queries(directory='tests/fixtures/test_queries/')


@pytest.fixture
def pg_conn_string():
    return 'postgresql://test:test@172.17.0.2:5432/test'


@pytest.fixture
def etl_object(mocker, pg_conn_string):
    def init_queries(self, directory='tests/fixtures/test_queries'):
        self.directory = directory
        self.query_dict = self._load_queries()

    mocker.patch('utils.queries.Queries.__init__', init_queries)
    mocker.patch.object(Config, 'create_connection', return_value=pg_conn_string)

    etl = ETL(save_path='tests/fixtures/test_etl/output/')
    etl.ROOMS = 'tests/fixtures/test_etl/input/test_rooms.json'
    etl.STUDENTS = 'tests/fixtures/test_etl/input/test_students.json'
    return etl

#
# @pytest.fixture(scope="function")
# def create_schema_fixture(etl_object):
#     etl_object.prepare_db()
#     yield
#     etl_object.db.execute_query("DROP SCHEMA IF EXISTS task_1 CASCADE")
#     etl_object.db._connect.commit()
#
#
# @pytest.fixture(scope="function")
# def etl_load_fixture(etl_object):
#     etl_object.extract()
#     etl_object.prepare_db()
#     yield
#     etl_object.db.execute_query("DROP SCHEMA IF EXISTS task_1 CASCADE")
#     etl_object.db._connect.commit()
