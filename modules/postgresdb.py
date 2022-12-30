from __future__ import annotations

from typing import Literal

import pandas as pd
import psycopg2 as ps
from sqlalchemy import create_engine


class Postgres:
    """
    The Postgres class is a utility class that contains various
    methods for interacting with a PostgreSQL database.
    It has five methods: __init__, execute_query, create_schema,
    write_dataframe_to_database, and get_df_from_db.

    Args:
        db_config: str, credentials to connect to the database

    Attributes:
        engine: SQLAlchemy engine object for interacting with the database
        engine_connect: connection object for interacting with the database using the engine object
        _connect: connection object for interacting with the database using the psycopg2 library
        _cursor: cursor object for executing queries on the database
    """

    def __init__(self, db_config: str):
        """
        Create engine, connect and cursor objects to work with database

        Args:
            db_config: credentials to connect

        Returns:
            Engine, connect and cursor objects
        """
        self._connect = ps.connect(db_config)
        self._cursor = self._connect.cursor()
        self.engine = create_engine(db_config)
        self.engine_connect = self.engine.connect()

    def execute_query(self, query: str, **kwargs):
        """
        Execute a database operation

        Args:
            query: SQL query,
            **kwargs: **kwargs

        Returns:
            The method returns None. If an execute_query was executed,
            the returned values can be retrieved using fetch*() methods
        """
        return self._cursor.execute(query, **kwargs)

    def create_schema(self, statement: str | None):
        """
        Creates database schema

        Args:
            statement: SQL query

        Returns:
            The method returns None
        """
        return self.engine_connect.execute(statement)

    @staticmethod
    def write_dataframe_to_database(df: pd.DataFrame, db_config: str, table_name=None, schema=None) -> Literal[True]:
        """
        Writes DataFrame object into database

        Args:
            df: pandas DataFrame object
            db_config: credentials to connect
            table_name: name of the table, by default is None
            schema: name of the schema, by default is None

        Returns:
            True if executed
        """
        df.to_sql(
            name=table_name,
            con=db_config,
            schema=schema,
            if_exists='replace',
            index=False,
        )
        return True

    def get_df_from_db(self, statement=None) -> pd.DataFrame:
        """
        Get DataFrame object from the database using SQL query

        Args:
            statement: SQL query

        Returns:
            Pandas DataFrame object
        """
        return pd.read_sql(statement, self.engine_connect)
