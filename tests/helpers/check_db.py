from __future__ import annotations

import time

import psycopg2


def check_database_up(conn_string: str, max_attempts: int = 20, interval: float = 0.2) -> bool:
    """
    Check if a database is up and running by trying to connect to it and execute a simple query.

    Args:
        conn_string (str): The connection string for the database.
        max_attempts (int): The maximum number of attempts to connect to the database.
        interval (float): The interval between each attempt, in seconds.

    Returns:
        bool: True if the database is up and running, False otherwise.
    """
    attempt = 0
    while True:
        try:
            with psycopg2.connect(conn_string) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT 1')
                    result = cursor.fetchone()
                    if result:
                        return True
                    else:
                        return False
        except Exception as e:
            print(e)
            time.sleep(interval)
            attempt += 1
            if attempt >= max_attempts:
                raise Exception(f'Failed to connect to the database after {max_attempts} attempts')
