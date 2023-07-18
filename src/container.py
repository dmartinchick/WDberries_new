from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from config import Config
from database import Database


class Container(containers.DeclarativeContainer):

    # wiring_config = containers.WiringConfiguration(modules=[".endpoints"])
    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)
