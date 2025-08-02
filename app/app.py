from app.routers import hello_routers
from fastapi import FastAPI

app = FastAPI()
app.include_router(hello_routers.router, prefix="/api/v1/hello")
