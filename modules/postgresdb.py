from __future__ import annotations

import json
from datetime import date, datetime

import pandas as pd
import psycopg2 as ps
from db_config import Config
from sqlalchemy import create_engine

from utils.queries import Queries


class Postgres:

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
