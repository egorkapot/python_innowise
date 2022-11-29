from __future__ import annotations

import logging
from datetime import date

import pandas as pd

from configs.conf_db import Config
from modules.postgresdb import Postgres
from utils.queries import Queries

ROOMS = 'source/input_data/rooms.json'
STUDENTS = 'source/input_data/students.json'


logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')

if __name__ == '__main__':

    db_config = Config().get_config()
    db = Postgres(db_config)
    queries = Queries.get_query_dict()

    db.create_schema(queries.get('schema'))

    logging.debug('Schema was created')

    rooms_df = pd.read_json(ROOMS)
    students_df = pd.read_json(STUDENTS)
    students_df['birthday'] = pd.to_datetime(students_df['birthday'])
    db.write_dataframe_to_database(
        df=students_df, db_config=db_config, table_name='students', schema='task_1',
    )
    db.write_dataframe_to_database(
        df=rooms_df, db_config=db_config, table_name='rooms', schema='task_1',
    )

    logging.debug('Dataframes were created and loaded to database')

    for query_name, query in queries.items():
        if query_name != 'schema':
            result_df = db.get_df_from_db(query)
            result_df.to_json(path_or_buf=f'./source/output_data/{query_name}_result.json', orient='table')

    logging.debug('Dataframes were loaded to JSONs')
