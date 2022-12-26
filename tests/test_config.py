from __future__ import annotations

import pytest

from configs.conf_db import Config


def test_can_instantiate_config_json():
    Config(path='tests/fixtures/config_test.json')


def test_config_can_read_json(connection_string_result):
    conn_string = Config(path='tests/fixtures/config_test.json').create_connection()
    assert connection_string_result == conn_string


def test_can_not_create_config_if_path_is_incorrect():
    with pytest.raises(FileNotFoundError):
        Config(path='somepath')


def test_can_not_create_config_if_source_is_incorrect():
    with pytest.raises(ValueError):
        Config(source='somesource')
