from __future__ import annotations

from typing import Literal
from typing import Optional

import pandas as pd
import psycopg2 as ps
from sqlalchemy import create_engine


class Postgres:
    """
    Postgres class that contains ETL functions

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

    def query(self, query: str, **kwargs):
        """
        Execute a database operation

        Args:
            query: SQL query,
            **kwargs: **kwargs

        Returns:
            The method returns None. If a query was executed, the returned values can be retrieved using fetch*() methods
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

    def write_dataframe_to_database(self, df: pd.DataFrame, db_config: str, table_name=None, schema=None) -> Literal[True]:
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
        df = pd.read_sql(statement, self._connect)
        return df
