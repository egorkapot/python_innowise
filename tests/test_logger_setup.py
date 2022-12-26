from __future__ import annotations

from unittest.mock import patch

import pytest
import yaml

from logg.logger_setup import setup_logging


def test_setup_logging():
    with patch('logging.config.dictConfig') as mock_dictConfig:
        with open('tests/fixtures/test_config.yaml', 'w') as config_fout:
            yaml.dump({'logging_config': 'test_config'}, config_fout)
        setup_logging('tests/fixtures/test_config.yaml')
        mock_dictConfig.assert_called_once_with({'logging_config': 'test_config'})


def test_setup_logging_invalid_config():
    with open('test_config.yaml', 'w') as config_fout:
        config_fout.write('invalid yaml')
    with pytest.raises(ValueError):
        setup_logging('test_config.yaml')


def test_setup_logging_missing_config():
    with pytest.raises(FileNotFoundError):
        setup_logging('missing_config.yaml')
