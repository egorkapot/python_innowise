from __future__ import annotations

from abc import ABCMeta
from abc import abstractmethod


class ETL_Base(metaclass=ABCMeta):

    def __init__(self) -> None:
        """
        Initializing
        """
        pass

    @abstractmethod
    def extract(self):
        """
        Extracting the data
        """
        pass

    def prepare_db(self):
        """
        Preparing database
        """
        pass

    @abstractmethod
    def load(self):
        """
        Loading the data
        """
        pass

    def extract_query_results(self):
        """
        Extracting the data
        """
        pass

    def run(self):
        """
        Running the modules
        """
        pass
