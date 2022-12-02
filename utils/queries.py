from __future__ import annotations

import os


class Queries:
    """
    Contains dictionary of queries that extract the data from database
    """

    def __init__(self, directory='queries/'):
        """
        Initializing the directory, path and dict objects.
        Directory - location of the file
        Query_dict - dictionary object

        Args:
            directory: location of the file, queries/ by default

        Returns:
            None
        """
        self.directory = directory
        self.query_dict = dict()

    def get_query_dict(self) -> dict:
        """
        Getting dictionary with queries from class

        Args:
            None

        Returns:
            Dictionary with SQL queries
        """

        for filename in os.scandir(self.directory):
            if filename.is_file():
                name = filename.path.replace(self.directory, '').rstrip('.sql')
                with open(filename) as f_in:
                    string = f_in.read()
                    self.query_dict[name] = string
        return self.query_dict
