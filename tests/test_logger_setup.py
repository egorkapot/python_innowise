from __future__ import annotations

from unittest.mock import patch

import pytest
import yaml

from logg.logger_setup import setup_logging


@pytest.fixture
def config_logger():
    return 'tests/fixtures/test_config.yaml'


def test_setup_logging(config_logger):
    with patch('logging.config.dictConfig') as mock_dictConfig:
        with open(config_logger, 'w') as config_fout:
            yaml.dump({'logging_config': 'test_config'}, config_fout)
        setup_logging(config_logger)
        mock_dictConfig.assert_called_once_with({'logging_config': 'test_config'})


def test_setup_logging_invalid_config(config_logger):
    with pytest.raises(ValueError):
        setup_logging(config_logger)


def test_setup_logging_missing_config():
    with pytest.raises(FileNotFoundError):
        setup_logging('missing_config.yaml')
