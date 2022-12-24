from __future__ import annotations

from abc import ABCMeta
from abc import abstractmethod


class ETL_Base(metaclass=ABCMeta):
    """
    Abstract base class for ETL (extract, transform, load) processes.

    This class defines the common methods and attributes
    that all ETL classes should have, including the `extract`, `prepare_db`, and
    `load` methods, which should be implemented by subclasses. It also provides a
    `run` method for executing the ETL process and a `extract_query_results`
    method for extracting data from a database query.

    Args:
       metaclass: ABCMeta, the metaclass used to define the abstract base class
    """

    def __init__(self) -> None:
        """
        Initialize an ETL_Base object.

        Returns:
            None
        """
        pass

    @abstractmethod
    def extract(self):
        """
        Extract data from its source.

        This method should be implemented by subclasses.

        Returns:
            None
        """
        pass

    def prepare_db(self):
        """
        Prepare the database for data loading.

        Returns:
            None
        """
        pass

    @abstractmethod
    def load(self):
        """
        Load the extracted data into the destination.

        This method should be implemented by subclasses.

        Returns:
            None
        """
        pass

    def extract_query_results(self):
        """
        Extract the results of a database query.

        Returns:
            None
        """
        pass

    def run(self):
        """
        Run the ETL process.

        This method calls the `extract`, `prepare_db`, and `load` methods in order.

        Returns:
            None
        """
        pass
