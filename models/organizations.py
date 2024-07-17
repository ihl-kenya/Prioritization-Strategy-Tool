from sqlalchemy import Column, Integer, String
from .base import Base


class Organizations(Base):
    __tablename__ = "organizations"

    org_id = Column(String, primary_key=True, nullable=False, index=True)
    org_name = Column(String, index=True)
    org_level = Column(Integer, index=True)
    parent_id = Column(String, index=True)
    mfl_code = Column(Integer, index=True)
