from __future__ import annotations

import logging

import pandas as pd

from configs.conf_db import Config
from logg.logger_setup import setup_logging
from modules.base_etl_class import ETL_Base
from modules.postgresdb import Postgres
from utils.queries import Queries

DEFAULT_CONFIG_LOGGER = 'logg/logging_conf.yml'
APPLICATION_NAME = 'etl'
setup_logging(DEFAULT_CONFIG_LOGGER)
logger = logging.getLogger(APPLICATION_NAME)


class ETL(ETL_Base):
    """
    Conduction of ETL process considering creation the schema with tables in database

    Args:
        ROOMS: path to the file which needs to be loaded
        STUDENTS: path to the file which needs to be loaded
    """

    ROOMS = 'source/input_data/rooms.json'
    STUDENTS = 'source/input_data/students.json'

    def __init__(self) -> None:
        """
        Creating a connection, initializing a database object and receiving a dictionary with queries

        Args:
            None

        Returns:
            None
        """

        super().__init__()
        self.students_df = None
        self.rooms_df = None
        self.db_config = Config().create_connection()
        self.db = Postgres(self.db_config)
        self.queries = Queries().get_query_dict()
        logger.debug("Initialized object of ETL class")

    def extract(self):
        """
        Getting the dataframes from jsons

        Returns:
            None
        """
        self.rooms_df = pd.read_json(ETL.ROOMS)
        self.students_df = pd.read_json(ETL.STUDENTS)
        self.students_df['birthday'] = pd.to_datetime(self.students_df['birthday'])
        logger.debug('Dataframes were created')

    def prepare_db(self):
        """
        Creating a database schema with tables

        Returns:
            None
        """
        self.db.create_schema(self.queries.get('schema'))
        logger.debug('Schema was created')

    def load(self):
        """
        Loading dataframes to database

        Returns:
            None
        """
        self.db.write_dataframe_to_database(
            df=self.students_df, db_config=self.db_config, table_name='students', schema='task_1',
        )
        self.db.write_dataframe_to_database(
            df=self.rooms_df, db_config=self.db_config, table_name='rooms', schema='task_1',
        )

        logger.debug('Dataframes were loaded to database')

    def extract_query_results(self):
        """
        Writing SQL queries to database and loading the result to json

        Returns:
            None
        """
        for query_name, query in self.queries.items():
            if 'query' in query_name:
                result_df = self.db.get_df_from_db(query)
                result_df.to_json(path_or_buf=f'source/output_data/{query_name}_result.json', orient='table')

        logger.debug('Dataframes were loaded to JSONs')

    def run(self):
        """
        Running the modules
        """
        self.extract()
        self.prepare_db()
        self.load()
        self.extract_query_results()
        logger.debug("End of ETL process")
