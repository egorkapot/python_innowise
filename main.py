from __future__ import annotations

import json
from datetime import date
from datetime import datetime

import pandas as pd
import psycopg2 as ps
from sqlalchemy import create_engine

from db_config import get_config_string
from queries import Queries


class Postgres():

    # Инициализация дб
    def __init__(self, db_config):
        self._connect = ps.connect(db_config)
        self._cursor = self._connect.cursor()
        self.engine = create_engine(db_config)
        self.engine_connect = self.engine.connect()
        self.db_config = db_config

    # Будет обрабатывать запросы. В текущей таске не используется но считаю полезным ее оставить

    def query(self, query, **kwargs):
        return self._cursor.execute(query, **kwargs)

    # Создаю схему. Использую движок. В теории statement могу кинуть в class Queries
    def create_schema(self, statement):
        return self.engine_connect.execute(statement)

    # Гружу датафрейм в базу
    def write_dataframe_to_database(self, df, table_name=None, schema=None):
        df.to_sql(
            name=table_name,
            con=self.db_config,  # в их коде не работало
            schema=schema,
            if_exists='replace',
            index=False,
        )
        return True  # Код из примера. Тут нет смысла возвращать True но на будущее оставлю

    # Получаю датафреймы из SQL. Statement беру из class Queries
    def get_df_from_db(self, statement=None):
        df = pd.read_sql(statement, self._connect)
        return df

    # Загрузка в JSON c указанием имени файла
    def df_to_json(self, df, filename):
        # Я указываю формат table. Дока говорит что в таком формате dateformat будет ISO8601
        df.to_json(filename, orient='table')



db_config = get_config_string()
db = Postgres(db_config)
db.create_schema(Queries.schema)

print('Schema created')

rooms_df = pd.read_json('rooms.json')
students_df = pd.read_json('students.json')
students_df['birthday'] = pd.to_datetime(students_df['birthday'])
db.write_dataframe_to_database(
df=students_df, table_name='students', schema='task_1')
db.write_dataframe_to_database(
df=rooms_df, table_name='rooms', schema='task_1')
print('Dataframes were created and loaded to database')


list_of_rooms = db.get_df_from_db(Queries.query_list_of_rooms)
lowest_avg_age = db.get_df_from_db(Queries.query_lowest_avg_age)
age_diff = db.get_df_from_db(Queries.query_age_diff)
gender = db.get_df_from_db(Queries.query_gender)
print('Dataframes were created from queries')


db.df_to_json(list_of_rooms, 'list_of_rooms.json')
db.df_to_json(lowest_avg_age, 'lowest_avg_age.json')
db.df_to_json(age_diff, 'age_diff.json')
db.df_to_json(gender, 'gender.json')
print('JSONs were created')

