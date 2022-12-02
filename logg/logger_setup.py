from __future__ import annotations

import logging.config

import yaml


def setup_logging(config_logger):
    with open(config_logger) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))
