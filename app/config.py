import logging.config


from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Settings(BaseSettings):
    turso_db_url: str
    turso_db_auth_token: str
    logging_config: str = "./logging.config"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


def get_logger():
    return logging.getLogger(__name__)


db_url = f"sqlite+{settings.turso_db_url}/?authToken={settings.turso_db_auth_token}&secure=true"
engine = create_engine(db_url, connect_args={'check_same_thread': False}, echo=True)


def get_db():
    with Session(engine) as session:
        yield session
