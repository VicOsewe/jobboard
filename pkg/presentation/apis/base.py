from fastapi import APIRouter

from pkg.presentation.apis.rest import route_users
from pkg.presentation.apis.rest import route_jobs



api_router = APIRouter()
api_router.include_router(route_users.router,prefix="/users",tags=["users"])
api_router.include_router(route_jobs.router,prefix="/jobs",tags=["jobs"]) 