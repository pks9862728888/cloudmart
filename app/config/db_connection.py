from sqlalchemy import create_engine
import os

from app.config.logger import logger
from app.config.settings import settings

db_engine = create_engine(settings.db_url, echo=True)


def test_db_connection():
    logger.info("Establishing connection with db...")
    with db_engine.connect() as conn:
        logger.info("Connection with db success!")
        pass
