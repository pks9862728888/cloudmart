from app.config import settings
from app.config.logger import logger
from app.config import db_connection
from app.routers import hello_routers
from fastapi import FastAPI

logger.info(f"Active profile is: {settings.get_active_profile()}")
db_connection.test_db_connection()

app = FastAPI()
app.include_router(hello_routers.router, prefix="/api/v1/hello")
