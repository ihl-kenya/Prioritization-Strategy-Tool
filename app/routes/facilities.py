from fastapi import APIRouter, Depends
from app.schemas.facilities import Facility, MultipleFacilities, FacilityOwnership
from app.services.facilities import FacilityServices
from app.config import get_db
from sqlalchemy.orm import Session


def create_facility_router() -> APIRouter:
    facility_router = APIRouter(
        prefix="/facility", tags=["Facilities Endpoints"])
    facility_services = FacilityServices()

    @facility_router.get("/all/", response_model=list[Facility])
    async def get_facilities(start: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        facilities = facility_services.get_facilities(
            start=start, limit=limit, db=db)
        return facilities

    return facility_router
