from sqlalchemy import Column, String, Integer, Boolean
from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # username might not be necessary, we can let teams login with their emails and password
    # username = Column(String, index=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)  # research hashing method
    # should be enumerated
    access_level = Column(String, index=True, nullable=False)
    org_id = Column(String, index=True)
    approved = Column(Boolean)
