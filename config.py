from abc import ABC, abstractmethod
from dataclasses import dataclass
from environs import Env

env = Env()
env.read_env('.env')


class DbConfig(ABC):
    @abstractmethod
    def get_url(self):
        pass


@dataclass
class PgDbConfig(DbConfig):
    username: str
    password: str
    host: str
    port: str
    database_name: str

    def get_url(self):
        return f'postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database_name}'


@dataclass
class SQLliteDbConfig(DbConfig):
    db_name: str

    def get_url(self):
        return f"sqlite:///{self.db_name}"


class MySQLDbConfig(DbConfig):
    def get_url(self):
        pass
