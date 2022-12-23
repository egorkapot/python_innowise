from __future__ import annotations

from modules.etl import ETL

import logging


from logg.logger_setup import setup_logging


DEFAULT_CONFIG_LOGGER = 'logg/logging_conf.yml'
APPLICATION_NAME = 'etl'
setup_logging(DEFAULT_CONFIG_LOGGER)
logger = logging.getLogger(APPLICATION_NAME)

if __name__ == '__main__':
   
    logger.debug('Running ETL')
    ETL().run()
    logger.debug('fINISHED')

