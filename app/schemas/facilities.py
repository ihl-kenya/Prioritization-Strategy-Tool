from pydantic import BaseModel
from enum import Enum


class Facility(BaseModel):
    facility_id: int
    facility_name: str
    facility_ownership: str
    keph_level: str
    mfl_code: int | None
    workload: int
    org_id: str


class Organization(BaseModel):
    org_id: str | None
    org_name: str | None
    mfl_code: int | None


class FacilityOwnership(Enum):
    ownerships = ["Faith Based Organisation", "Private", "Ministry of Health"]
