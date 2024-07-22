from sqlalchemy.orm import Session
from models import Facilities, Organizations
from fastapi import HTTPException, status
from sqlalchemy import or_


class FacilityServices:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_facilities(*, start: int = 0, limit: int = 100, db: Session):
        try:
            facilities = db.query(Facilities).offset(start).limit(limit).all()
            return facilities
        except Exception as e:
            print(f"Error caused by: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not process request"
            )

    @staticmethod
    def get_facility(facility_id: str, db: Session):
        db_facility = db.query(Facilities)\
            .filter(Facilities.org_id == facility_id)\
            .first()
        if db_facility is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )
        return db_facility

    @staticmethod
    def get_organizations(
        org_id: str | None,
        org_name: str | None,
        mfl_code: int | None,
        db: Session
    ):
        query = db.query(Organizations)
        filters = []

        if org_id:
            filters.append(Organizations.org_id == org_id)
        if org_name:
            filters.append(Organizations.org_name == org_name)
        if mfl_code:
            filters.append(Organizations.mfl_code == mfl_code)

        if filters:
            query = query.filter(or_(*filters))
            facilities = query.all()
            if not facilities:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No Organizations were found with the given criteria"
                )
            return facilities
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No filtering values supplied"
        )
