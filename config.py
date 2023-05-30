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


@dataclass
class Proxies:
    url: str


class Config:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self, db_config: DbConfig, proxies: Proxies):
        self.db_config = db_config
        self.proxies = proxies

    @property
    def db_config(self):
        return self.__db_config

    @db_config.setter
    def db_config(self, config: DbConfig):
        self.__db_config = config

    @property
    def proxies(self):
        return self.__proxies

    @proxies.setter
    def proxies(self, proxies: Proxies):
        self.__proxies = proxies
