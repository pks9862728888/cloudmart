from fastapi import APIRouter


router = APIRouter(tags=["v1/hello"])


@router.get("/")
async def hello() -> dict:
    return {"message": "Hello, World!"}
