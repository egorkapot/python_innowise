from __future__ import annotations

import glob
import os

import pandas as pd
import pytest

from tests.helpers.check_db import check_database_up


@pytest.fixture()
def data_columns():
    return {
        'rooms': ('id', 'name'),
        'students': ('birthday', 'id', 'name', 'room', 'sex'),
    }


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
    CONN_STRING = 'postgresql://test:test@172.17.0.2:5432/test'
    os.system(
        'docker run --rm -d -p 5444:5444 -e POSTGRES_PASSWORD=test \
        -e POSTGRES_USER=test \
        -e POSTGRES_DB=test \
        --name pg_db postgres:latest',
    )
    while True:
        if check_database_up(CONN_STRING):
            break


def teardown_module():
    os.system('docker stop pg_db')


def test_instantiate_etl(etl_object, pg_conn_string):
    assert etl_object.db_config == pg_conn_string
    assert isinstance(etl_object.queries, dict)


def test_etl_extract(etl_object, data_columns):
    etl_object.extract()
    assert isinstance(etl_object.rooms_df, pd.DataFrame)
    assert isinstance(etl_object.students_df, pd.DataFrame)
    assert data_columns['rooms'] == tuple(etl_object.rooms_df.columns.tolist())
    assert data_columns['students'] == tuple(etl_object.students_df.columns.tolist())


def test_can_create_schema(etl_object, check_db_queries):
    etl_object.prepare_db()
    for query in check_db_queries:
        etl_object.db.execute_query(query)
        result = etl_object.db._cursor.fetchone()
        assert result


def test_etl_load(etl_object, etl_load_queries):
    etl_object.extract()
    etl_object.prepare_db()
    etl_object.load()
    for query in etl_load_queries:
        etl_object.db.execute_query(query)
        result = etl_object.db._cursor.fetchone()
        assert result


def test_extract_query_results(etl_object):
    etl_object.extract()
    etl_object.prepare_db()
    etl_object.load()
    etl_object.extract_query_results()
    assert len(etl_object.queries.keys()) - 1 == len(glob.glob(f'{etl_object.save_path}/*.json'))


def test_etl_run(etl_object):
    assert etl_object.run()
