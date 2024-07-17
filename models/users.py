from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)  # research hashing method
    access_level = Column(String, index=True, nullable=False)
    approved = Column(Boolean)
    org_id = Column(String, ForeignKey("organizations.org_id"), index=True)
