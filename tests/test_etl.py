from __future__ import annotations

import os

import pandas as pd
import pytest

from tests.helpers.check_db import check_database_up


@pytest.fixture()
def check_db_queries():
    return [
        "SELECT 1 FROM information_schema.schemata WHERE schema_name = 'task_1'",
        "SELECT 1 FROM information_schema.tables WHERE table_schema = 'task_1' AND table_name = 'rooms'",
        "SELECT 1 FROM information_schema.tables WHERE table_schema = 'task_1' AND table_name = 'students'",
    ]


@pytest.fixture()
def etl_load_queries():
    return [
        'SELECT 1 FROM task_1.rooms',
        'SELECT 1 FROM task_1.students',
    ]


def setup_module():
    os.system(
        'docker run --rm -d -p 5444:5444 -e POSTGRES_PASSWORD=test \
        -e POSTGRES_USER=test \
        -e POSTGRES_DB=test \
        --name pg_db postgres:latest',
    )
    pg_conn_string = 'postgresql://test:test@172.17.0.2:5432/test'
    while True:
        if check_database_up(pg_conn_string):
            break


def teardown_module():
    os.system('docker stop pg_db')


def test_instantiate_etl(etl_object, pg_conn_string):
    assert etl_object.db_config == pg_conn_string
    assert isinstance(etl_object.queries, dict)


def test_etl_extract(etl_object):
    etl_object.extract()
    assert isinstance(etl_object.rooms_df, pd.DataFrame)
    assert isinstance(etl_object.students_df, pd.DataFrame)
    assert ('id', 'name') == tuple(etl_object.rooms_df.columns.tolist())
    assert ('birthday', 'id', 'name', 'room', 'sex') == tuple(etl_object.students_df.columns.tolist())


def test_can_create_schema(etl_object, create_schema_fixture, check_db_queries):
    for query in check_db_queries:
        etl_object.db.execute_query(query)
        result = etl_object.db._cursor.fetchone()
        assert result


def test_etl_load(etl_object, etl_load_fixture, etl_load_queries):
    etl_object.load()
    for query in etl_load_queries:
        etl_object.db.execute_query(query)
        result = etl_object.db._cursor.fetchone()
        assert result
