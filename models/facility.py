from sqlalchemy import Column, String, Integer
from .base import Base


class Facility(Base):
    __tablename__ = "facilities"

    key = Column(Integer, primary_key=True, autoincrement=True)
    facility_id = Column(String, unique=True, index=True, nullable=False)
    facility_name = Column(String, index=True)
    facility_ownership = Column(String, nullable=True)
    mfl_code = Column(Integer, nullable=True)
    keph_level = Column(String, nullable=False, index=True)
    workload = Column(Integer)
