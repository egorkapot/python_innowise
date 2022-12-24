from __future__ import annotations

import logging.config

import yaml


def setup_logging(config_logger: str) -> None:
    """
    Set up logging using the specified configuration file.

    Args:
        config_logger: str, path to the logging configuration file

    Returns:
        None
    """
    with open(config_logger) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))
