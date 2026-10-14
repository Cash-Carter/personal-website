# Copyright 2026 Cash Carter
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import about, contact, projects, root

logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format="%(levelname)s:%(name)s:%(asctime)s: %(message)s")

logger.info("Creating FastAPI app")
app: FastAPI = FastAPI()
logger.info("Including routers")
app.include_router(about.router)
app.include_router(contact.router)
app.include_router(projects.router)
app.include_router(root.router)
logger.info("Mounting static files")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
