from __future__ import annotations

from modules.etl import ETL
from modules.etl import logger

if __name__ == '__main__':
    logger.debug('Start ETL process')
    ETL().run()
    logger.debug('Finish programm')
