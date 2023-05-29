import os
import pytest
from config import PgDbConfig, SQLliteDbConfig


class TestConfig:

    @pytest.mark.parametrize(
        "username, password, host, port, db_name, expected_result",
        [
            ('scott',
             'test_password',
             'localhost',
             '0000',
             'test_db',
             "postgresql+psycopg2://scott:test_password@localhost:0000/test_db"),
            ('test',
             'pass',
             'superhost',
             '1123',
             'super_db',
             "postgresql+psycopg2://test:pass@superhost:1123/super_db")
        ]
    )
    def test_pg_get_url(self, username, password, host, port, db_name, expected_result):
        config = PgDbConfig(username=username,
                            password=password,
                            host=host,
                            port=port,
                            database_name=db_name)
        assert config.get_url() == expected_result

    def test_file_env_is_exists(self):
        assert os.path.exists('../.env')

    def test_mysql_get_url(self):
        pass

    @pytest.mark.parametrize(
        'db_name, expected_result',
        [('foo.db', 'sqlite:///foo.db'),
         ('test.db', "sqlite:///test.db")]
    )
    def test_sqllite_get_url(self, db_name, expected_result):
        config = SQLliteDbConfig(db_name=db_name)
        assert config.get_url() == expected_result
