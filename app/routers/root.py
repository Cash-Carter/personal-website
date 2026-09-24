import logging
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse

logger = logging.getLogger(__name__)

router: APIRouter = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def get_root():
    logger.debug("Returning index.html")
    with open("app/html/index.html") as file:
        return file.read()
