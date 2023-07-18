from contextlib import contextmanager, AbstractContextManager
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from app import logger


Base = declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> ... | AbstractContextManager[Session]:
        sesion: Session = self._session_factory()
        try:
            yield sesion
        except Exception:
            logger.exception("Session rollback because of exeption")
            sesion.rollback()
            raise
        finally:
            sesion.close()
