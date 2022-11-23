import json
from datetime import date, datetime
from sqlalchemy import create_engine
import pandas as pd
import psycopg2 as ps
from db_config import get_config_string

#наследственный класс который по идее должен возвращать запросы
class Queries:

    def __init__(self):
    #Нужно ли прописывать инит для этого класса чтобы объекты определялись в классе?
    
        self.query_select_rooms = """
        SELECT *
        FROM task_1.rooms
        """

        self.query_select_students = """
        SELECT *
        FROM task_1.students
        """

        self.query_list_of_rooms = """
        SELECT r.name as room, COUNT(*) as number_of_students
        FROM task_1.rooms r
        JOIN task_1.students s ON r.id = s.room
        GROUP BY r.name
        ORDER BY number_of_students DESC
        """

        #Запрос возвращает timestamp
        #Фикстится использованием date_trunc
        self.query_lowest_avg_age = """
        SELECT r.name as room, DATE_TRUNC('day', AVG(AGE(s.birthday))) AS average_age
        FROM task_1.students s
        JOIN task_1.rooms r
        ON s.room = r.id
        GROUP BY r.name
        ORDER BY average_age 
        LIMIT 5
        """

        self.query_age_diff = """
        SELECT s2.room, AGE(s2.max_date, s2.min_date) as age_diff
        FROM(
        SELECT room, MAX(birthday) OVER(PARTITION BY room) as max_date, 
        MIN(birthday) OVER(PARTITION BY room) as min_date
        FROM task_1.students)s2
        GROUP BY s2.room, AGE(s2.max_date, s2.min_date)
        ORDER BY age_diff DESC
        LIMIT 5
        """

        self.query_gender = """
        SELECT room
        FROM task_1.students
        GROUP BY room
        HAVING MIN(sex)<> MAX(sex)
            """

class Postgres(Queries): 
    
    #Инициализация дб
    def __init__(self, db_config):
        self._connect = ps.connect(db_config)
        self._cursor = self._connect.cursor()
        self.engine = create_engine(db_config)
        self.engine_connect = self.engine.connect()
        self.db_config = db_config


    #Будет обрабатывать запросы. В текущей таске не используется но считаю полезным ее оставить
    def query(self, query, **kwargs):
        return self._cursor.execute(query, **kwargs)

    #Создаю схему. Использую движок. В теории statement могу кинуть в class Queries
    def create_schema(self):

        statement = """CREATE SCHEMA IF NOT EXISTS task_1;
                    CREATE TABLE IF NOT EXISTS task_1.rooms (
                    id int PRIMARY KEY, 
                    name VARCHAR(50));
                    CREATE TABLE IF NOT EXISTS task_1.students (
                        birthday DATE,
                        id int,
                        name VARCHAR(60), 
                        room int, 
                        sex CHAR(1),
                        FOREIGN KEY (room) REFERENCES task_1.rooms(id) ON DELETE CASCADE);"""
        return self.engine_connect.execute(statement)

    #Гружу датафрейм в базу
    def write_dataframe_to_database(self, df, table_name=None, schema=None):
        df.to_sql(
            name=table_name,
            con=self.db_config, #в их коде не работало
            schema=schema,
            if_exists="replace",
            index=False
        )        
        return True #Код из примера. Тут нет смысла возвращать True но на будущее оставлю
    
    #Получаю датафреймы из SQL. Statement беру из class Queries
    def get_df_from_db(self, statement=None):
        df = pd.read_sql(statement, self._connect)
        return df
    
    #Загрузка в JSON c указанием имени файла
    def df_to_json(self, df, filename):
        df.to_json(filename, orient='table') #Я указываю формат table. Дока говорит что в таком формате dateformat будет ISO8601


try:
    db_config = get_config_string()
    db = Postgres(db_config)
    db.create_schema()

    print('Schema created')
    try:
        rooms_df = pd.read_json('rooms.json')
        students_df = pd.read_json('students.json')
        students_df['birthday'] = pd.to_datetime(students_df['birthday'])   
        db.write_dataframe_to_database(df=students_df, table_name='students', schema='task_1')
        db.write_dataframe_to_database(df=rooms_df, table_name='rooms', schema='task_1')
        print('Dataframes were created and loaded to database')

        try:
            list_of_rooms = db.get_df_from_db(Queries().query_list_of_rooms)
            lowest_avg_age = db.get_df_from_db(Queries().query_lowest_avg_age)
            age_diff = db.get_df_from_db(Queries().query_age_diff)
            gender = db.get_df_from_db(Queries().query_gender)
            print('Dataframes were created from queries')

            try:
                db.df_to_json(list_of_rooms, 'list_of_rooms.json')
                db.df_to_json(lowest_avg_age, 'lowest_avg_age.json')
                db.df_to_json(age_diff, 'age_diff.json')
                db.df_to_json(gender, 'gender.json')
                print('JSONs were created')

            except:
                print('Error was caused while creating JSONs')
        except:
            print('Error was caused while creating databases from queries')
    except:
        print('Error was caused while uploading dataframes to database')       
except:
    print('Something with creating a schema')

