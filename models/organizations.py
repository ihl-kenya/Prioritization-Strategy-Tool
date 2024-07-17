from sqlalchemy import Column, Integer, String
from .base import Base


class Organizations(Base):
    __tablename__ = "organizations"

    key = Column(Integer, primary_key=True, autoincrement=True)
    org_id = Column(String)
    org_name = Column(String)
    org_level = Column(Integer)
    parent_id = Column(String)
