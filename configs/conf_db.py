from __future__ import annotations

import json
import os


class Config:

    """
    Creating a configuration to connect to database
    """

    def __init__(self, source='json') -> None:
        """
        Creating a config string based on the input source.
        If source is json - takes the credentials from config.json file located in configs directory
        If source is env - takes the credentials from the environment which were preuploaded from .envrc file
        """

        if source == 'json':
            with open('configs/config.json') as f:
                config = json.load(f)

            db_name = config['CONFIGURATION']['DATABASE_NAME']
            db_type = config['CONFIGURATION']['DB_TYPE']
            db_host = config['CONFIGURATION']['HOST_ADDRESS']
            db_port = config['CONFIGURATION']['PORT']
            db_user = config['CONFIGURATION']['DB_USER']
            db_password = config['CONFIGURATION']['DB_PASSWORD']

        elif source == 'env':
            db_name = os.environ.get('DATABASE_NAME')
            db_type = os.environ.get('DB_TYPE')
            db_host = os.environ.get('HOST_ADDRESS')
            db_port = os.environ.get('PORT')
            db_user = os.environ.get('DB_USER')
            db_password = os.environ.get('DB_PASSWORD')

        self.db_config = f'{db_type}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    def get_config(self) -> str:
        """
        Getting config from class

        Returns:
            String with credentials for connection
        """
        return self.db_config
