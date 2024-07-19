from sqlalchemy.orm import Session
from models import Facilities
from fastapi import HTTPException, status


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
