from __future__ import annotations

import json
import os


class Config:

    """
    Creating a configuration to connect to database
    """

    def __init__(self, source='json', path='configs/config.json') -> None:
        """
        Creating a config string based on the input source.
        If source is json - takes the credentials from config.json file located in configs directory
        If source is env - takes the credentials from the environment which were preuploaded from .envrc file

        Args:
            source: string with source type, by default is JSON

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
        Getting config from class

        Args:
            None

        Returns:
            String with credentials for connection
        """
        self.db_config = f'{self.db_type}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'


        return self.db_config
