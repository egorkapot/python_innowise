from __future__ import annotations

import psycopg2 as ps
import pytest

from modules.postgresdb import Postgres


def test_can_not_instantiate_postgres_dbconfig_is_none():
    with pytest.raises(ps.OperationalError):
        Postgres(db_config=None)


def test_can_not_instantiate_postgres_dbconfig_is_int():
    with pytest.raises(TypeError):
        Postgres(db_config=1)


def test_can_not_instantiate_postgres_dbconfig_is_invalid():
    with pytest.raises(ps.ProgrammingError):
        Postgres(db_config='some_config')
