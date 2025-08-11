from app.config import settings
from app.config.logger import logger
from app.config import db_connection
from app.routers import project_router
from app.routers import frontend_router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

logger.info(f"Active profile is: {settings.get_active_profile()}")
db_connection.test_db_connection()

app = FastAPI()
app.mount("/_next/", StaticFiles(directory="public/_next"), name="nextjs_assets")
app.mount("/static", StaticFiles(directory="public"), name="static")
app.include_router(project_router.router, prefix="/api/v1/project")
app.include_router(frontend_router.router, prefix="")
