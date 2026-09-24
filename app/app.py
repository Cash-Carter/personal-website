import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import root

logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format="%(levelname)s:%(name)s:%(asctime)s: %(message)s")

logger.info("Creating FastAPI app")
app: FastAPI = FastAPI()
logger.info("Includeing routers")
app.include_router(root.router)
logger.info("Mounting static files")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
