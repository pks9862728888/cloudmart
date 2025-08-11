import os
from fastapi import APIRouter, Path
from fastapi.responses import FileResponse


router = APIRouter(tags=["frontend"])


@router.get("/")
@router.get("/{page:str}")
async def serve_spa(page: str):
    print(f"{page}")
    file_path = f"public/{page}"

    # Check if resource exists
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)

    # Check if HTML file can be resolved
    if not file_path.endswith(".html"):
        html_path = f"{file_path}.html"
        print(f"htmlpath: {html_path}")
        if os.path.exists(html_path):
            return FileResponse(html_path)

    # Fallback to 404.html
    return FileResponse("public/404.html")
