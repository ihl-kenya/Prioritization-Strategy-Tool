from sqlalchemy import Column, String, Integer, ForeignKey, Float
from .base import Base


class Allocations(Base):
    __tablename__ = "allocations"

    key = Column(Integer, primary_key=True, autoincrement=True)
    facility_id = Column(String, ForeignKey("facilities.facility_id"))
    facility_name = Column(String, index=True, nullable=False)
    facility_workload = Column(Integer, nullable=False)
    allocated_amt = Column(Float, nullable=False)
