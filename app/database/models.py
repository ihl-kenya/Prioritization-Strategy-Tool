from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

# Classes that interact with the database


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # username might not be necessary, we can let teams login with their emails and password
    # username = Column(String, index=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)  # research hashing method
    # should be enumerated
    access_level = Column(String, index=True, nullable=False)


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True,
                        autoincrement=True, index=True)
    product_name = Column(String, index=True, nullable=False)
    product_category = Column(String, index=True, nullable=False)
    ven = Column(String, nullable=False)
    is_equipment = Column(Boolean)
    kmfl_classification = Column(String)
    is_rmnch = Column(Boolean)
    is_in_647_tracer_list = Column(Boolean)


class Facility(Base):
    __tablename__ = "facilities"

    key = Column(Integer, primary_key=True, autoincrement=True)
    facility_id = Column(String, unique=True, index=True, nullable=False)
    facility_name = Column(String, index=True)
    mfl_code = Column(Integer, unique=True, index=True, nullable=True)
    keph_level = Column(String, nullable=False,
                        index=True)  # should be enumerated
    ward = Column(String, nullable=False, index=True)
    ward_id = Column(String, nullable=False)
    sub_county = Column(String, nullable=False, index=True)
    sub_county_id = Column(String, nullable=False)
    county = Column(String, nullable=False, index=True)
    county_id = Column(String)


class Forecast(Base):
    __tablename__ = "forecasts"

    key = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    pack_size = Column(String)
    price_kes = Column(Float)
    quantity_required_for_one_year = Column(Float)
    facility_id = Column(Integer, ForeignKey("facilities.facility_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
