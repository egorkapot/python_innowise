from __future__ import annotations

import json
import os


class Config:
    """
     The Config class is used to create a configuration object for
     connecting to a database. It has two methods: __init__ and create_connection.
     """

    __slots__ = ['db_name', 'db_type', 'db_host', 'db_port', 'db_user', 'db_password']

    def __init__(self, source='json', path='configs/config.json') -> None:
        """
        Initialize a new Config object.

        Args:
            source: string with source type, either 'json' or 'env' (default: 'json')
            path: string with the path to the JSON configuration file (default: 'configs/config.json')

        Returns:
            None
        """
        if source == 'json':
            with open(path) as f:
                config = json.load(f)
            self.db_name = config['CONFIGURATION']['DATABASE_NAME']
            self.db_type = config['CONFIGURATION']['DB_TYPE']
            self.db_host = config['CONFIGURATION']['HOST_ADDRESS']
            self.db_port = config['CONFIGURATION']['PORT']
            self.db_user = config['CONFIGURATION']['DB_USER']
            self.db_password = config['CONFIGURATION']['DB_PASSWORD']
        elif source == 'env':
            self.db_name = os.environ.get('DATABASE_NAME')
            self.db_type = os.environ.get('DB_TYPE')
            self.db_host = os.environ.get('HOST_ADDRESS')
            self.db_port = os.environ.get('PORT')
            self.db_user = os.environ.get('DB_USER')
            self.db_password = os.environ.get('DB_PASSWORD')
        else:
            raise ValueError('Expected json or env file')

    def create_connection(self) -> str:
        """
        Return a string with the credentials

        Returns:
            String with credentials for connection
        """
        return f'{self.db_type}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
