from pydantic import BaseModel
from enum import Enum


class Facility(BaseModel):
    facility_id: int
    facility_name: str
    facility_ownership: str
    keph_level: str
    mfl_code: int | None
    # workload: int
    org_id: str


class MultipleFacilities(BaseModel):
    facilities: list[Facility]


class FacilityOwnership(Enum):
    ownerships = ["Faith Based Organisation", "Private", "Ministry of Health"]
