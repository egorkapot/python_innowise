from __future__ import annotations

import os


class Queries():
    """
    Contains dictionary of queries that extract the data from database
    """
    _query_dict = dict()

    @classmethod
    def get_query_dict(cls) -> dict:
        """
        Getting dictionary with queries from class

        Args:
            None

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
