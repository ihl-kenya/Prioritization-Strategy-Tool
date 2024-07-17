from sqlalchemy import Column, String, Integer
from .base import Base


class Facility(Base):
    __tablename__ = "facilities"

    facility_id = Column(Integer, primary_key=True)
    facility_name = Column(String, index=True)
    facility_ownership = Column(String)
    keph_level = Column(String, nullable=False, index=True)
    mfl_code = Column(Integer, index=True)
    workload = Column(Integer)
    org_id = Column(String, index=True)
