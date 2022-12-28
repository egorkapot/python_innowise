from __future__ import annotations

import os

import pandas as pd

from tests.helpers.check_db import check_database_up


# def setup_module():
#     # Open a connection
#     os.system('docker run --rm -d -p 5444:5444 -e POSTGRES_PASSWORD=test \
#         -e POSTGRES_USER=test \
#         -e POSTGRES_DB=test \
#         --name pg_db postgres:latest')
#     pg_conn_string = 'postgresql://test:test@172.17.0.2:5432/test'
#     while True:
#         if check_database_up(pg_conn_string):
#             break


# def teardown_module():
#     # Close the connection
#     os.system('docker stop pg_db')


def test_instantiate_etl(etl_object, pg_conn_string):

    # Verify that the mock config was used to create the database object
    assert etl_object.db_config == pg_conn_string
    assert isinstance(etl_object.queries, dict)


def test_etl_extract(etl_object):

    etl_object.extract()
    assert isinstance(etl_object.rooms_df, pd.DataFrame)
    assert isinstance(etl_object.students_df, pd.DataFrame)
    assert ('id', 'name') == tuple(etl_object.rooms_df.columns.tolist())
    assert ('birthday', 'id', 'name', 'room', 'sex') == tuple(etl_object.students_df.columns.tolist())


def test_can_create_schema(etl_object):
    etl_object.prepare_db()
