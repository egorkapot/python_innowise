from __future__ import annotations

import os
from typing import Dict


class Queries:
    """
    A utility class for managing a collection of SQL queries.

    This class allows you to load SQL queries from a directory and store them in a dictionary.
    The queries can then be accessed by name and used to execute database operations.

    Args:
        directory: Path to the directory containing the query files.
    """

    def __init__(self, directory='queries'):
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
        self.query_dict = self._load_queries()

    def _load_queries(self) -> Dict[str, str]:
        """
        Load queries from the directory into a dictionary.

        Returns:
            Dictionary of query names and SQL strings.
        """
        query_dict = {}
        for filename in os.scandir(self.directory):
            if filename.is_file():
                name = filename.path.replace(self.directory, '').rstrip('.sql')
                with open(filename) as f_in:
                    string = f_in.read()
                    query_dict[name] = string
        return query_dict
