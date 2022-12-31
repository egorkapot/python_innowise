from __future__ import annotations

import os
import re
from mmap import ACCESS_READ
from mmap import mmap


class Queries:
    """
    A utility class for managing a collection of SQL queries.

    This class allows you to load SQL queries from a directory and store them in a dictionary.
    The queries can then be accessed by name and used to execute database operations.

    Args:
        directory: Path to the directory containing the execute_query files.
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

    def _load_queries(self) -> dict[str, str]:
        """
        Load queries from the directory into a dictionary.

        Returns:
            Dictionary of query names and SQL strings.
        """
        query_dict = {}
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    with mmap(f.fileno(), 0, access=ACCESS_READ) as m:
                        name, _ = os.path.splitext(filename)
                        query = m.read().decode().strip()
                        query = query.replace('\t', ' ')
                        query = re.sub(r'\s+', ' ', query)
                        query = re.sub(r'\n+', ' ', query)
                        query_dict[name] = query

        return query_dict
