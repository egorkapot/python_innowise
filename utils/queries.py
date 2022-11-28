from __future__ import annotations

import os
from typing import Dict


class Queries():

    """
        Contains dictionary of queries that extract the data from database
    """

    _query_dict = dict()

    @classmethod
    def get_query_dict(cls) -> dict:
        """
        Getting dictionary with queries from class

        Returns:
            Dictionaty with SQL queries
        """

        for filename in os.scandir('queries'):
            if filename.is_file():
                name = filename.path.lstrip('queries').replace('/', '').rstrip('.sql')
                with open(filename) as f_in:
                    string = f_in.read()
                    cls._query_dict[name] = string
        return cls._query_dict

    #     with open (sql_file, 'r') as f_in:
    #         string = f_in.read()

    #     query_select_rooms = string("queries/query_select_rooms.sql")
    #     query_select_students = string("queries/query_select_students.sql")
    #     query_list_of_rooms = string("queries/query_list_of_rooms.sql")
    #     query_lowest_avg_age = string("queries/query_lowest_avg_age.sql")
    #     query_age_diff = string("queries/query_age_diff.sql")
    #     query_gender = string("queries/query_gender.sql")
    #     schema = string("queries/schema.sql")

    # query_select_rooms = """
    # SELECT *
    # FROM task_1.rooms
    # """

    # query_select_students = """
    # SELECT *
    # FROM task_1.students
    # """

    # query_list_of_rooms = """
    # SELECT r.name as room, COUNT(*) as number_of_students
    # FROM task_1.rooms r
    # JOIN task_1.students s ON r.id = s.room
    # GROUP BY r.name
    # ORDER BY number_of_students DESC
    # """

    # # Запрос возвращает timestamp
    # # Фикстится использованием date_trunc
    # query_lowest_avg_age = """
    # SELECT r.name as room, DATE_TRUNC('day', AVG(AGE(s.birthday))) AS average_age
    # FROM task_1.students s
    # JOIN task_1.rooms r
    # ON s.room = r.id
    # GROUP BY r.name
    # ORDER BY average_age
    # LIMIT 5
    # """

    # query_age_diff = """
    # SELECT s2.room, AGE(s2.max_date, s2.min_date) as age_diff
    # FROM(
    # SELECT room, MAX(birthday) OVER(PARTITION BY room) as max_date,
    # MIN(birthday) OVER(PARTITION BY room) as min_date
    # FROM task_1.students)s2
    # GROUP BY s2.room, AGE(s2.max_date, s2.min_date)
    # ORDER BY age_diff DESC
    # LIMIT 5
    # """

    # query_gender = """
    # SELECT room
    # FROM task_1.students
    # GROUP BY room
    # HAVING MIN(sex)<> MAX(sex)
    #     """

    # schema = """
    # CREATE SCHEMA IF NOT EXISTS task_1;
    # CREATE TABLE IF NOT EXISTS task_1.rooms (
    # id int PRIMARY KEY,
    # name VARCHAR(50));
    # CREATE TABLE IF NOT EXISTS task_1.students (
    #     birthday DATE,
    #     id int,
    #     name VARCHAR(60),
    #     room int,
    #     sex CHAR(1),
    #     FOREIGN KEY (room) REFERENCES task_1.rooms(id) ON DELETE CASCADE);
    #     """
