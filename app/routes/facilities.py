from fastapi import APIRouter, Depends, Query
from app.schemas.facilities import Facility, Organization
from app.services.facilities import FacilityServices
from app.config import get_db
from sqlalchemy.orm import Session
from models import Facilities


def create_facility_router() -> APIRouter:
    facility_router = APIRouter(
        prefix="/facilities", tags=["Facilities Endpoints"])
    facility_services = FacilityServices()

    @facility_router.get("/all/", response_model=list[Facility], status_code=200)
    async def get_facilities(start: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        facilities = facility_services.get_facilities(
            start=start, limit=limit, db=db)
        return facilities

    @facility_router.get("/hierarchy", response_model=list[Organization], status_code=200)
    async def get_organization(
        org_id: str | None = Query(None),
        org_name: str | None = Query(None),
        mfl_code: int | None = Query(None),
        db: Session = Depends(get_db)
    ):
        facilities = facility_services.get_organizations(
            org_id=org_id,
            org_name=org_name,
            mfl_code=mfl_code,
            db=db
        )
        return facilities

    @facility_router.get("/{facility_id}", response_model=Facility, status_code=200)
    async def get_facility(facility_id: str, db: Session = Depends(get_db)):
        facility = facility_services.get_facility(
            facility_id=facility_id, db=db)
        return facility

    return facility_router
