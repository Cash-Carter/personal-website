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
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from templates import templates

logger = logging.getLogger(__name__)

router: APIRouter = APIRouter()

@router.get("/projects", response_class=HTMLResponse)
async def get_projects():
    logger.debug("Returning projects")
    with open("app/html/projects.html") as file:
        return templates.get_template("header_and_footer.html").render(content=file.read())