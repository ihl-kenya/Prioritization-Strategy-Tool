from fastapi import APIRouter


def create_facility_routers() -> APIRouter:
    facility_router = APIRouter(
        prefix="/facilities", tags=["Facilities Endpoints"])

    return facility_router
