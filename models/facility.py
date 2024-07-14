from sqlalchemy import Column, String, Integer
from .base import Base


class Facility(Base):
    __tablename__ = "facilities"

    key = Column(Integer, primary_key=True, autoincrement=True)
    facility_id = Column(String, unique=True, index=True, nullable=False)
    facility_name = Column(String, index=True)
    mfl_code = Column(Integer, unique=True, index=True, nullable=True)
    keph_level = Column(String, nullable=False, index=True)
    ward = Column(String, nullable=False, index=True)
    ward_id = Column(String, nullable=False)
    sub_county = Column(String, nullable=False, index=True)
    sub_county_id = Column(String, nullable=False)
    county = Column(String, nullable=False, index=True)
    county_id = Column(String)
