from __future__ import annotations

import pandas as pd

from configs.conf_db import Config
from modules.postgresdb import Postgres
from utils.queries import Queries

ROOMS = 'source/input_data/rooms.json'
STUDENTS = 'source/input_data/students.json'


if __name__ == '__main__':

    db_config = Config().get_config()
    db = Postgres(db_config)
    db.create_schema(Queries.schema)

    print('Schema created')

    rooms_df = pd.read_json(ROOMS)
    students_df = pd.read_json(STUDENTS)
    students_df['birthday'] = pd.to_datetime(students_df['birthday'])
    db.write_dataframe_to_database(
        df=students_df, db_config=db_config,  table_name='students', schema='task_1',
    )
    db.write_dataframe_to_database(
        df=rooms_df, db_config=db_config, table_name='rooms', schema='task_1',
    )

    print('Dataframes were created and loaded to database')

    list_of_rooms = db.get_df_from_db(Queries.query_list_of_rooms)
    lowest_avg_age = db.get_df_from_db(Queries.query_lowest_avg_age)
    age_diff = db.get_df_from_db(Queries.query_age_diff)
    gender = db.get_df_from_db(Queries.query_gender)
    print('Dataframes were created from queries')

    db.df_to_json(list_of_rooms, 'source/output_data/rooms.json')
    db.df_to_json(lowest_avg_age, 'source/output_data/lowest_avg_age.json')
    db.df_to_json(age_diff, 'source/output_data/age_diff.json')
    db.df_to_json(gender, 'source/output_data/gender.json')
    print('JSONs were created')
